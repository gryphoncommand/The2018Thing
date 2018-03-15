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

        main_pov = oi.joystick.getPOV()
        assist_pov = oi.assist_joystick.getPOV()
        
        pov = -1

        if main_pov != -1:
            pov = main_pov
        else:
            pov = assist_pov

        if pov != -1:

            if pov in (0, 180):
                subsystems.arm.set_final_extender(False)

            if pov in (45, 90, ):
                subsystems.arm.set_final_extender(False)
            if pov in (270, 180+45):
                subsystems.arm.set_final_extender(True)

            if pov in (0, 45, 90):
                subsystems.arm.set_extender(True)
            if pov in (180, 180+45, 270):
                subsystems.arm.set_extender(False)

    def end(self):
        subsystems.arm.set_extender(False)
