import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing

class DriveToDistance(Command):
    def __init__(self, _ldist, _rdist):
        self.ldist = _ldist
        self.rdist = _rdist
        subsystems.tankdrive.encoders["L"].useDistance()
        subsystems.tankdrive.encoders["R"].useDistance()
        self.LPID = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2], pid.dist_L[3], subsystems.tankdrive.encoders["L"], subsystems.tankdrive.set_left)
        self.RPID = PIDController(pid.dist_R[0], pid.dist_R[1], pid.dist_R[2], pid.dist_R[3], subsystems.tankdrive.encoders["R"], subsystems.tankdrive.set_right)

        self.applyPID(lambda p: p.setPIDSourceType(PIDController.PIDSourceType.kRate))
        self.applyPID(lambda p: p.setOutputRange(-1, 1))
        self.applyPID(lambda p: p.setContinuous(False))

    def update_pid(self):
        gearing = subsystems.tankdrive.get_gearing()
        lrange = 0.0
        rrange = 0.0

        if gearing == Gearing.LOW:
            self.pid["L"].setInputRange(*robotmap.drive_encoders.L_L)
            self.pid["R"].setInputRange(*robotmap.drive_encoders.R_L)
            lrange = abs(robotmap.drive_encoders.L_L[1] - robotmap.drive_encoders.L_L[0])
            rrange = abs(robotmap.drive_encoders.R_L[1] - robotmap.drive_encoders.R_L[0])
            
        elif gearing == Gearing.HIGH:
            self.pid["L"].setInputRange(*robotmap.drive_encoders.L_H)
            self.pid["R"].setInputRange(*robotmap.drive_encoders.R_H)
            lrange = abs(robotmap.drive_encoders.L_H[1] - robotmap.drive_encoders.L_H[0])
            rrange = abs(robotmap.drive_encoders.R_H[1] - robotmap.drive_encoders.R_H[0])

        self.pid["L"].setAbsoluteTolerance(lrange / 10.0)
        self.pid["R"].setAbsoluteTolerance(rrange / 10.0)

    def applyPID(self, func):
        func(self.pid["L"])
        func(self.pid["R"])

    def initalize(self):
        self.applyPID(lambda pid: pid.enable())
        self.LPID.setSetpoint(subsystems.tankdrive.encoders["L"].getDistance() + self.ldist)
        self.RPID.setSetpoint(subsystems.tankdrive.encoders["R"].getDistance() + self.rdist)
        subsystems.tankdrive.set_gearing(Gearing.LOW)

    def execute(self):
        wpilib.SmartDashboard.putData("Distance L PID", self.LPID)
        wpilib.SmartDashboard.putData("Distance R PID", self.RPID)

    def isFinished(self):
        return self.LPID.onTarget() & self.RPID.onTarget()

    def interrupted(self):
        self.end()

    def end(self):
        self.applyPID(lambda pid: pid.enable())
