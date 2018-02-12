import time

from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi
from pid.pidmotor import PIDMotorSource, PIDMotorOutput

from puremath.scaling import transform

import robotmap
from robotmap import axes, pid, Gearing
import wpilib
import math


class PIDTankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """


    def __init__(self):
        super().__init__('PIDTankDriveJoystick')

        self.requires(subsystems.tankdrive)

        self.pid = {}
        self.l_src = PIDMotorSource(subsystems.tankdrive.encoders["L"], robotmap.drive_encoders.L_H, robotmap.drive_encoders.L_L)
        self.r_src = PIDMotorSource(subsystems.tankdrive.encoders["R"], robotmap.drive_encoders.R_H, robotmap.drive_encoders.R_L)
       
        self.l_out = PIDMotorOutput([subsystems.tankdrive.motors["LF"], subsystems.tankdrive.motors["LB"]])
        self.r_out = PIDMotorOutput([subsystems.tankdrive.motors["RF"], subsystems.tankdrive.motors["RB"]])
        
        self.pid["L"] = PIDController(pid.L[0], pid.L[1], pid.L[2], pid.L[3], self.l_src, self.l_out)
        self.pid["R"] = PIDController(pid.R[0], pid.R[1], pid.R[2], pid.R[3], self.r_src, self.r_out)
        # self.pid["L"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        # self.pid["R"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        
        # self.applyPID(lambda p: p.setPIDSourceType(PIDController.PIDSourceType.kRate))
        self.applyPID(lambda p: p.setOutputRange(-1, 1))


    def update_pid(self):
        gearing = subsystems.tankdrive.get_gearing()
        if gearing == Gearing.LOW:
            self.pid["L"].setInputRange(*robotmap.drive_encoders.L_L)
            self.pid["R"].setInputRange(*robotmap.drive_encoders.R_L)
        elif gearing == Gearing.HIGH:
            self.pid["L"].setInputRange(*robotmap.drive_encoders.L_H)
            self.pid["R"].setInputRange(*robotmap.drive_encoders.R_H)

    def initialize(self):
        self.applyPID(lambda pid: pid.enable())
        self.applyPID(lambda pid: pid.setContinuous(False))
        self.applyPID(lambda pid: pid.setAbsoluteTolerance(0.1))
        

    def applyPID(self, func):
        func(self.pid["L"])
        func(self.pid["R"])

    def execute(self):
        self.update_pid()

        joy = oi.joystick
        lpow = joy.getRawAxis(axes.L_y)
        rpow = joy.getRawAxis(axes.R_y)
        
        wpilib.SmartDashboard.putString("tankdrive", str((lpow, rpow)))

        gearing = subsystems.tankdrive.get_gearing()
        wpilib.SmartDashboard.putString("Gearing", str(gearing))
        if gearing == Gearing.LOW:
            lpow = transform(lpow, (1, -1), robotmap.drive_encoders.L_L)
            rpow = transform(rpow, (1, -1), robotmap.drive_encoders.R_L)
            self.pid["L"].setSetpoint(lpow)
            self.pid["R"].setSetpoint(rpow)
        elif gearing == Gearing.HIGH:
            lpow = transform(lpow, (-1, 1), robotmap.drive_encoders.L_H)
            rpow = transform(rpow, (-1, 1), robotmap.drive_encoders.R_H)
            self.pid["L"].setSetpoint(lpow)
            self.pid["R"].setSetpoint(rpow)
        wpilib.SmartDashboard.putString("tankdrive2", str((lpow, rpow)))
        wpilib.SmartDashboard.putNumber("L PID Setpoint", self.pid["L"].getSetpoint())
        wpilib.SmartDashboard.putNumber("R PID Setpoint", self.pid["R"].getSetpoint())
        wpilib.SmartDashboard.putData("L PID", self.pid["L"])
        wpilib.SmartDashboard.putData("R PID", self.pid["R"])


    def end(self):
        self.applyPID(lambda pid: pid.disable())
