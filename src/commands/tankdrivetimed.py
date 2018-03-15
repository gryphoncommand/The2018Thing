import time

from wpilib.command import Command

import subsystems
import oi
import time

from robotmap import axes

class TankDriveTimed(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self, lspeed, rspeed, tlen):
        super().__init__('TankDriveTimed')
        self.lspeed, self.rspeed, self.tlen = lspeed, rspeed, tlen

        self.requires(subsystems.tankdrive)
        self.stime = None

    def initialize(self):
        self.stime = time.time()

    def execute(self):
        subsystems.tankdrive.set(self.lspeed, self.rspeed)

    def end(self):
        subsystems.tankdrive.set(0, 0)
    
    def isFinished(self):
        return self.stime is not None and time.time() - self.stime > self.tlen

    def interrupted(self):
        self.end()
