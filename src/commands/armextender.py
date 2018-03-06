import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes

from puremath import Vector2D


class ArmExtender(Command):
    """

    Controls the arm with the POV

    """

    def __init__(self):
        super().__init__('ArmExtender')

        #self.requires(subsystems.arm)

    def initialize(self):
        pass

    def execute(self):

        pov = oi.joystick.getPOV()
        
        if pov != -1:
            if pov in (0, 45, 90):
                subsystems.arm.set_extender(True)
            if pov in (180, 180+45, 270):
                subsystems.arm.set_extender(False)

            if pov in (45, 90, ):
                subsystems.arm.set_final_extender(False)
            if pov in (270, 180+45):
                subsystems.arm.set_final_extender(True)


    def end(self):
        subsystems.arm.set_extender(False)
