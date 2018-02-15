import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing
from pid.pidnavx import PIDNavxSource


class DriveToDistance(Command):
    def __init__(self, _angle):
        self.angle = _angle
        self.navx = PIDNavxSource(subsystems.sensors.navx)
        self.PID = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2], pid.dist_L[3], self.navx, subsystems.tankdrive.set)

        self.PID.setPIDSourceType(PIDController.PIDSourceType.kRate)
        self.PID.setInputRange(-180, 180)
        self.PID.setOutputRange(-1, 1)
        self.PID.setContinuous(True)
        self.PID.setAbsoluteTolerance(4)

    def initalize(self):
        val = self.navx.pidGet() = self.angle
        if val > 180:
            val -=360
        elif val < -180:
            val += 360
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
