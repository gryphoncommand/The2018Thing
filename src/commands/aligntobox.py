import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing
from networktables import NetworkTables
from pid.pidnt import PIDnt


'''
PARAMS:
The distance is in meters.
Remember
1 meter = 3.28084 feet.
1 meter = 39.3701 inches.
PID Source
PID Output
'''


class AlignToBox(Command):
    def __init__(self):
        super().__init__('AlignToBox')

        # PIDSource Init
        self.source = PIDnt("centerX", "Radius")

        self.PID = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2],
                                 pid.dist_L[3], self.source,
                                 subsystems.tankdrive.set)
        self.PID.setInputRange(0, 1)
        self.PID.setOutputRange(-1, 1)
        self.PID.setContinuous(False)

        self.PID.setAbsoluteTolerance(.01)

    def initialize(self):
        subsystems.tankdrive.set_gearing(Gearing.LOW)
        self.PID.enable()
        self.PID.setSetpoint(0.5)

    def execute(self):
        wpilib.SmartDashboard.putData("Vision PID", self.PID)
        if self.PID.onTarget():
            self.end()

    def end(self):
        self.PID.disable()

    def isFinished(self):
        return self.PID.onTarget()

    def interrupted(self):
        self.end()
