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
        self.toggle = False


    def initialize(self):
        pass
    
    
    def execute(self):
        # if self.param == True: 
        #     self.toggle = False
        # else:
        #     self.toggle = True        
        
        # if self.toggle:
        #     arm_power = -1
        # else:
        #     arm_power = 0
        rot_power = (oi.joystick.getRawAxis(axes.R_t) - oi.joystick.getRawAxis(axes.L_t)) / 2.0
        subsystems.arm.set_rotator(rot_power)
    
        # subsystems.arm.set_wench(wench_power)


    def end(self):
        subsystems.arm.set_rotator(0.0)
