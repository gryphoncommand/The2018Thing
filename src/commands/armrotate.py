import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes


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
        rot_power = (oi.joystick.getRawAxis(axes.R_t) - oi.joystick.getRawAxis(axes.L_t)) / 2.0
       # print(subsystems.arm.rotator_encoders["R"])

        subsystems.smartdashboard.putNumber("rot_encoder", subsystems.arm.get_arm_proportion())
        subsystems.smartdashboard.putNumber("rot_angle", subsystems.arm.get_arm_angle())
        subsystems.smartdashboard.putNumber("rot_power", rot_power)

        #if ticks <= 0 and rot_power < 0:
        #    subsystems.arm.set_rotator(0)
        #else:
        #    subsystems.arm.set_rotator(rot_power)
        subsystems.arm.set_rotator(rot_power, raw=False)

    def end(self):
        subsystems.arm.stop_rotator()
