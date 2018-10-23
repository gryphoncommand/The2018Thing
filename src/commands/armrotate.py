import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes


class ArmRotate(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('TankDriveJoystick')

        self.requires(subsystems.arm)

    def initialize(self):
        pass

    def execute(self):
        rot_power = (oi.joystick.getRawAxis(axes.R_t) - oi.joystick.getRawAxis(axes.L_t)) / 2.0

        subsystems.smartdashboard.putNumber("rot_power", rot_power)

        subsystems.arm.set_rotator(rot_power)

    def end(self):
        subsystems.arm.stop_rotator()
