import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing

'''
PARAMS:
The distance is in meters.
Remember 
1 meter = 3.28084 feet.
1 meter = 39.3701 inches.
'''


class DriveToDistance(Command):
    def __init__(self, _ldist, _rdist):
        self.ldist = _ldist
        self.rdist = _rdist

        self.pid = {}
        self.pid["L"] = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2], pid.dist_L[3], subsystems.tankdrive.encoders["L"], subsystems.tankdrive.set_left)
        self.pid["R"] = PIDController(pid.dist_R[0], pid.dist_R[1], pid.dist_R[2], pid.dist_R[3], subsystems.tankdrive.encoders["R"], subsystems.tankdrive.set_right)

    def update_pid(self):
        gearing = subsystems.tankdrive.get_gearing()

        self.applyPID(lambda p: p.setOutputRange(-1, 1))
        self.applyPID(lambda p: p.setContinuous(False))
        self.applyPID(lambda p: p.useDistance())
        
        subsystems.tankdrive.set_gearing(Gearing.LOW)

        self.pid["L"].setAbsoluteTolerance(.1)
        self.pid["R"].setAbsoluteTolerance(.1)

        self.applyPID(lambda pid: pid.enable())
        

    def applyPID(self, func):
        func(self.pid["L"])
        func(self.pid["R"])

    def initalize(self):
        self.update_pid()
        
        self.LPID.setSetpoint(subsystems.tankdrive.encoders["L"].getDistance() + self.ldist)
        self.RPID.setSetpoint(subsystems.tankdrive.encoders["R"].getDistance() + self.rdist)


    def end(self):
        self.applyPID(lambda pid: pid.disable())


    def execute(self):
        self.update_pid()

        wpilib.SmartDashboard.putData("L Distance PID", self.pid["L"])
        wpilib.SmartDashboard.putData("R Distance PID", self.pid["R"])

    def isFinished(self):
        return self.pid["L"].onTarget() and self.pid["R"].onTarget()

    def interrupted(self):
        self.end()
