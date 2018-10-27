import wpilib

from wpilib.command import Command
import time
import subsystems

class DoNothing(Command):
    def __init__(self, _duration=None):
        super().__init__('DoNothing')
        self.duration = _duration

    def initialize(self):
        self.start = time.time()

    def execute(self):
        #pass
        subsystems.tankdrive.set(0, 0)
        # subsystems.arm.set_rotator(0)

    def isFinished(self):
        return (time.time() - self.start) > self.duration

