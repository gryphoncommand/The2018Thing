import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes

class TankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('TankDriveJoystick')

        self.requires(subsystems.tankdrive)

    def initialize(self):
        pass

    def execute(self):
        lpow = oi.joystick.getRawAxis(axes.L_y)
        rpow = oi.joystick.getRawAxis(axes.R_y)

        subsystems.tankdrive.set(lpow, rpow)

        subsystems.smartdashboard.putString("tankdrive", str((lpow, rpow)))

    def end(self):
        subsystems.tankdrive.set(0, 0)
