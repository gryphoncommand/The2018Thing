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
        joy = oi.get_joystick()
        lpow = joy.getRawAxis(axes.L_y)
        rpow = joy.getRawAxis(axes.R_y)

        subsystems.tankdrive.set(lpow, rpow)

        subsystems.smartdashboard.putString("tankdrive", str((lpow, rpow)))
        # subsystems.smartdashboard.putNumber("Ticks", subsystems.tankdrive.encoders["L"].get())

    def end(self):
        subsystems.tankdrive.set(0, 0)
