import wpilib

from wpilib.command import Command
import subsystems

class RunIntake(Command):
    def __init__(self, speed):
        self.speed = speed

    def initalize(self):
        self.isDone = False

    def execute(self):
        subsystems.arm.set_rotator(speed)
        self.isDone = True
    
    def end(self):
        subsystems.arm.set_rotator(0.0)

    def isFinished(self):
        return self.isDone
