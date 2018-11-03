import wpilib

from wpilib.command import Command
import subsystems

class RunIntake(Command):
    def __init__(self, speed):
        self.speed = speed

    def initalize(self):
        super().__init__('RunIntake[%s]' % speed)
        self.isDone = False
        self.requires(subsystems.arm)


    def execute(self):
        subsystems.arm.set_rotator(speed)
        self.isDone = True
    
    def end(self):
        subsystems.arm.set_rotator(0.0)

    def isFinished(self):
        return self.isDone
