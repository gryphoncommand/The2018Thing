import time

from wpilib.command import Command

import subsystems

from commands.drivedist import DriveToDistance
from commands.turndrive import TurnDrive

class Sequence(Command):
    """

    This dumps the info

    """

    def __init__(self):
        super().__init__('Sequence')

        self.cmds = []

        self.addSequential(DriveToDistance(1, 1))
        self.addSequential(TurnDrive(90))
        self.addSequential(DriveToDistance(1, 1))
        self.addSequential(TurnDrive(90))
        self.addSequential(DriveToDistance(1, 1))


    def addSequential(self, cmd):
        self.cmds += [cmd]

    def initialize(self):
        self.c_i = 0
        self.has_init_c = False

    def execute(self):
        if not self.isFinished():
            if not self.has_init_c:
                self.cmds[self.c_i].initialize()
                self.has_init_c = True

            if self.cmds[self.c_i].isFinished():
                self.cmds[self.c_i].end()
                self.c_i += 1
                self.has_init_c = False
            else:
                self.cmds[self.c_i].execute()

    def isFinished(self):
        return self.c_i >= len(self.cmds)
        

