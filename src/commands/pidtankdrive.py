import time

from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi
from pid.pidmotor import PIDMotorSource, PIDMotorOutput

from robotmap import axes, pid
import wpilib


class PIDTankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('PIDTankDriveJoystick')

        self.requires(subsystems.tankdrive)

        self.L_sour = PIDMotorSource(subsystems.tankdrive.encoders["L"])
        self.R_sour = PIDMotorSource(subsystems.tankdrive.encoders["R"])

        self.addToPID(self.L_sour, self.R_sour,
                      lambda source: source.useSpeed())
        self.addToPID(self.L_sour, self.R_sour,
                      lambda source: source.setScale(-1))

        self.Lout = PIDMotorOutput([subsystems.tankdrive.motors["LF"],
                                    subsystems.tankdrive.motors["LB"]])
        self.Rout = PIDMotorOutput([subsystems.tankdrive.motors["RF"],
                                    subsystems.tankdrive.motors["RB"]])

        self.addToPID(self.Lout, self.Rout, lambda output: output.setScale(-1))

        self.LPID = PIDController(pid.L_P, pid.L_I, pid.L_D, pid.L_F,
                                  self.L_sour, self.Lout)
        self.RPID = PIDController(pid.R_P, pid.R_I, pid.R_D, pid.R_F,
                                  self.R_sour, self.Rout)

        self.addToPID(self.LPID, self.RPID,
                      lambda pid: pid.setInputRange(-3.5, 3.5))
        self.addToPID(self.LPID, self.RPID,
                      lambda pid: pid.setOutputRange(-1, 1))

    def initialize(self):
        pass

    def addToPID(self, pid1, pid2, func):
        func(pid1)
        func(pid2)

    def execute(self):
        if True:
            self.addToPID(self.LPID, self.RPID, lambda pid: pid.enable())
            self.normalOperation()

    def normalOperation(self):
        if True:
            wpilib.SmartDashboard.putData("L PID", self.LPID)
            wpilib.SmartDashboard.putData("R PID", self.RPID)
            # wpilib.LiveWindow.addSensor("Ticks", "Left Encoder",
            #                             subsystems.tankdrive.encoders["L"])
            # wpilib.LiveWindow.addSensor("Ticks", "Right Encoder",
            #                            subsystems.tankdrive.encoders["R"])
            wpilib.SmartDashboard.putNumber("Left Encoder", subsystems.tankdrive.encoders["L"].getRate())
            wpilib.SmartDashboard.putNumber("Right Encoder", subsystems.tankdrive.encoders["R"].getRate())


        joy = oi.get_joystick()
        self.lpow = joy.getRawAxis(axes.L_y)
        self.rpow = joy.getRawAxis(axes.R_y)
        # subsystems.tankdrive.set(lpow, rpow)
        if subsystems.tankdrive.gearshift.get():
            self.LPID.setSetpoint(-self.lpow * 3.5)
            self.RPID.setSetpoint(-self.rpow * 3.5)
        else:
            self.LPID.setSetpoint(-self.lpow * 1.4)
            self.RPID.setSetpoint(-self.rpow * 1.4)
        wpilib.SmartDashboard.putString("tankdrive",
                                        str((self.lpow, self.rpow)))

    def end(self):
        self.addToPID(self.LPID, self.RPID, lambda pid: pid.disable())