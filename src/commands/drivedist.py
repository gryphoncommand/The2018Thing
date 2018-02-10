import wpilib

from wpilib.command import Command

class DriveToDistance(Command):
    def __init__(self, _dist):
        self.dist = _dist

    def initalize(self):
        pass

    def execute(self):
        wpilib.SmartDashboard.putData("Distance PID", self.PID)

    def isFinished(self):
        pass

    def interrupted(self):
        self.end()

    def end(self):
        self.PID.disable()