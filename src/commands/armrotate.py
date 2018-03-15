import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes, joystick_info


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
        main_arm_power = (oi.joystick.getRawAxis(axes.R_t) - oi.joystick.getRawAxis(axes.L_t)) / 2.0
        assist_arm_power = (oi.assist_joystick.getRawAxis(axes.R_t) - oi.assist_joystick.getRawAxis(axes.L_t)) / 2.0

        if abs(main_arm_power) <= joystick_info.error:
            main_arm_power = 0
        if abs(assist_arm_power) <= joystick_info.error:
            assist_arm_power = 0
       # print(subsystems.arm.rotator_encoders["R"])

        #if ticks <= 0 and rot_power < 0:
        #    subsystems.arm.set_rotator(0)
        #else:
        #    subsystems.arm.set_rotator(rot_power)
        if main_arm_power < joystick_info.error:
            subsystems.arm.set_rotator(assist_arm_power, raw=False)
        else:
            subsystems.arm.set_rotator(main_arm_power, raw=False)

    def end(self):
        subsystems.arm.set_rotator(0.0)
