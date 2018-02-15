import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing
from pid.pidnavx import PIDNavXSource


class TurnDrive(Command):
    def __init__(self, _angle):
        self.angle = _angle
        self.navx = PIDNavXSource(subsystems.sensors.navx)
        self.PID = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2], pid.dist_L[3], self.navx, subsystems.tankdrive.set)

        self.PID.setInputRange(-180, 180)
        self.PID.setOutputRange(-1, 1)
        self.PID.setContinuous(True)
        self.PID.setAbsoluteTolerance(4)

    def initalize(self):
        self.val = self.navx.pidGet() + self.angle
        if self.val > 180:
            self.val -=360
        elif self.val < -180:
            self.val += 360
        self.PID.enable()
        self.PID.setSetpoint(val)

    def execute(self):
        wpilib.SmartDashboard.putData("Angle PID", self.PID)

    def isFinished(self):
        return self.PID.onTarget()

    def interrupted(self):
        self.end()

    def end(self):
        self.PID.disable()
        subsystems.tankdrive.stop()
