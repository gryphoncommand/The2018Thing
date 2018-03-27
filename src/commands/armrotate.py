import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes, joystick_info, buttons


class ArmRotate_reset(Command):

    def __init__(self):
        super().__init__('ArmRotate_reset')

        # self.requires(subsystems.arm)



    def initialize(self):
        subsystems.arm.reset_enc()

    def execute(self):
        pass

    def isFinished(self):
        return True

class ArmRotate(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('TankDriveJoystick')

        # self.requires(subsystems.arm)

    def initialize(self):
        pass

    def execute(self):
        arm_power = (oi.joystick.getRawAxis(axes.R_t) - oi.joystick.getRawAxis(axes.L_t)) / 2.0

        if abs(arm_power) <= joystick_info.error:
            arm_power = 0

        subsystems.arm.set_rotator(arm_power, raw=False)

        wench_power = 0.0

        if oi.joystick.getRawButton(buttons.TRIANGLE):
            wench_power = -1.0
        elif oi.joystick.getRawButton(buttons.X):
            wench_power = 1.0
        
        subsystems.arm.set_wench(wench_power)


    def end(self):
        subsystems.arm.set_rotator(0.0)
