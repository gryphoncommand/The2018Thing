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
        joy = oi.get_joystick()

        pov = joy.getPOV()

        if pov != -1:
            vec = Vector2D.from_polar(angle=pov + 90, degrees=True)
            if vec.y > 0.01:
                subsystems.arm.extender.set(True)
            elif vec.y < 0.01:
                subsystems.arm.extender.set(False)

    def end(self):
        subsystems.arm.extender.set(False)
