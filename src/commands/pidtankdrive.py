import time

from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi
from pid.pidmotor import PIDMotorSource, PIDMotorOutput

from puremath.scaling import transform

from robotmap import axes, pid
import wpilib


class PIDTankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """


    def __init__(self):
        super().__init__('PIDTankDriveJoystick')

        self.requires(subsystems.tankdrive)

        self.L_src = PIDMotorSource()
        self.R_src = PIDMotorSource(subsystems.tankdrive.encoders["R"])

        self.pid = {}

        self.pid["L"] = PIDController(1, 0, 0, self.encoders["L"].get, subsystems.tankdrive.set_left)
        self.pid["R"] = PIDController(1, 0, 0, self.encoders["R"].get, subsystems.tankdrive.set_right)

        
        self.applyPID(lambda p: p.setPIDSourceType(PIDController.PIDSourceType.kRate))
        self.applyPID(lambda p: p.setOutputRange(-1, 1))


    def update_pid(self):
        gearing = subsystems.tankdrrobotmap.drive_encoders.L_Live.get_gearing()
        if gearing == robotmap.Gearing.LOW:
            self.pid["L"].setInputRange(*robotmap.drive_encoders.L_L)
            self.pid["R"].setInputRange(*robotmap.drive_encoders.R_L)
        elif gearing == robotmap.Gearing.HIGH:
            self.pid["L"].setInputRange(*robotmap.drive_encoders.L_H)
            self.pid["R"].setInputRange(*robotmap.drive_encoders.R_H)


    def initialize(self):
        self.applyPID(lambda pid: pid.enable())

    def applyPID(self, func):
        func(self.pid["L"])
        func(self.pid["R"])

    def execute(self):
        wpilib.SmartDashboard.putData("L PID", self.pid["L"])
        wpilib.SmartDashboard.putData("R PID", self.pid["R"])
        # wpilib.LiveWindow.addSensor("Ticks", "Left Encoder",
        #                             subsystems.tankdrive.encoders["L"])
        # wpilib.LiveWindow.addSensor("Ticks", "Right Encoder",
        #                            subsystems.tankdrive.encoders["R"])
        wpilib.SmartDashboard.putNumber("Left Encoder", subsystems.tankdrive.encoders["L"].getRate())
        wpilib.SmartDashboard.putNumber("Right Encoder", subsystems.tankdrive.encoders["R"].getRate())


        joy = oi.joystick
        lpow = joy.getRawAxis(axes.L_y)
        rpow = joy.getRawAxis(axes.R_y)

        wpilib.SmartDashboard.putString("tankdrive", str((lpow, rpow)))

        gearing = subsystems.tankdrrobotmap.drive_encoders.L_Live.get_gearing()
        if gearing == robotmap.Gearing.LOW:
            lpow = transform(lpow, (-1, 1), robotmap.drive_encoders.L_L)
            rpow = transform(rpow, (-1, 1), robotmap.drive_encoders.R_L)
            self.pid["L"].setSetpoint(lpow)
            self.pid["R"].setSetpoint(rpow)
        elif gearing == robotmap.Gearing.HIGH:
            lpow = transform(lpow, (-1, 1), robotmap.drive_encoders.L_H)
            rpow = transform(rpow, (-1, 1), robotmap.drive_encoders.R_H)
            self.pid["L"].setSetpoint(lpow)
            self.pid["R"].setSetpoint(rpow)

    def end(self):
        self.applyPID(lambda pid: pid.disable())

