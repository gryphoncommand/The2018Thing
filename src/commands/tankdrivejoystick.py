import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes
import wpilib

class TankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('TankDriveJoystick')

        self.requires(subsystems.tankdrive)

    def initialize(self):
        self.lmax = 0
        self.rmax = 0

    def execute(self):
        lpow = oi.joystick.getRawAxis(axes.L_y)
        rpow = oi.joystick.getRawAxis(axes.R_y)

        if self.lmax > subsystems.tankdrive.encoders["L"].getRate():
            self.lmax = subsystems.tankdrive.encoders["L"].getRate()
        if self.rmax > subsystems.tankdrive.encoders["R"].getRate():
            self.rmax = subsystems.tankdrive.encoders["R"].getRate()

        wpilib.SmartDashboard.putNumber("Left Encoder Low", self.lmax)
        wpilib.SmartDashboard.putNumber("Right Encoder Low", self.rmax)

        subsystems.tankdrive.set(lpow, rpow)

        subsystems.smartdashboard.putString("tankdrive", str((lpow, rpow)))

    def end(self):
        subsystems.tankdrive.set(0, 0)
