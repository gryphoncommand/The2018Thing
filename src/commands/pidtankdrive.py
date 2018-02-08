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
        self.L_sour.useSpeed()
        self.R_sour.useSpeed()
        self.L_sour.setScale(-1)
        self.R_sour.setScale(-1)

        self.Lout = PIDMotorOutput([subsystems.tankdrive.motors["LF"],
                                    subsystems.tankdrive.motors["LB"]])
        self.Rout = PIDMotorOutput([subsystems.tankdrive.motors["RF"],
                                    subsystems.tankdrive.motors["RB"]])
        self.Lout.setScale(-1)
        self.Rout.setScale(-1)

        self.LPID = PIDController(pid.L_P, pid.L_I, pid.L_D, pid.L_F,
                                  self.L_sour, self.Lout)
        self.LPID.setInputRange(-(3.5), 3.5)
        self.LPID.setOutputRange(-1, 1)

        self.RPID = PIDController(pid.R_P, pid.R_I, pid.R_D, pid.R_F,
                                  self.R_sour, self.Rout)
        self.RPID.setInputRange(-(3.5), 3.5)
        self.RPID.setOutputRange(-1, 1)

    def initialize(self):
        self.RPID.enable()
        self.LPID.enable()

    def execute(self):
        if True:
            self.normalOperation()

    def normalOperation(self):
        if True:
            wpilib.SmartDashboard.putData("L PID", self.LPID)
            wpilib.SmartDashboard.putData("R PID", self.RPID)

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
        subsystems.smartdashboard.putString("tankdrive", str((self.lpow, self.rpow)))

    def end(self):
        self.LPID.disable()
        self.RPID.disable()
