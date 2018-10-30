import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes

from puremath import Vector2D


class AutoArmExtender(Command):
    """

    Controls the arm with the POV

    """

    def __init__(self, status):
        super().__init__('AutoArmExtender[%s]' % status)
        self.status = status
        self.requires(subsystems.arm)

    def initialize(self):
        self.is_init = False

    def execute(self):
        subsystems.arm.set_extender(self.status)
        self.is_init = True
    
    def isFinished(self):
        return self.is_init

    def end(self):
        self.is_init = False
    
    def interrupted(self):
        self.end()
