
import time

import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing


class ParametricDrive(Command):
    def __init__(self, _ldist, _rdist, timeout):
        super().__init__('ParametricDrive')

        # these should be lambda t: t as a setpoint for distance
        self.ldist = _ldist
        self.rdist = _rdist

        self.timeout = timeout

        self.pid = {}
        self.pid["L"] = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2], pid.dist_L[3], subsystems.tankdrive.encoders["L"], subsystems.tankdrive.set_left)
        self.pid["R"] = PIDController(pid.dist_R[0], pid.dist_R[1], pid.dist_R[2], pid.dist_R[3], subsystems.tankdrive.encoders["R"], subsystems.tankdrive.set_right)

    def update_pid(self):
        gearing = subsystems.tankdrive.get_gearing()

        self.applyPID(lambda p: p.setInputRange(-10**8, 10**8))
        self.applyPID(lambda p: p.setOutputRange(-1, 1))
        self.applyPID(lambda p: p.setContinuous(False))
        #self.applyPID(lambda p: p.useDistance())
        self.applyPID(lambda p: p.setPIDSourceType(PIDController.PIDSourceType.kDisplacement))
        
        subsystems.tankdrive.set_gearing(Gearing.LOW)

        self.pid["L"].setAbsoluteTolerance(.03)
        self.pid["R"].setAbsoluteTolerance(.03)

        
    def applyPID(self, func):
        func(self.pid["L"])
        func(self.pid["R"])

    def initialize(self):
        self.update_pid()
        self.applyPID(lambda pid: pid.enable())

        self.start_time = time.time()

        self.start_ldist = subsystems.tankdrive.encoders["L"].getDistance()
        self.start_rdist = subsystems.tankdrive.encoders["R"].getDistance()


    def execute(self):
        self.update_pid()

        dt = time.time() - self.start_time

        lset = self.start_ldist + self.ldist(dt)
        rset = self.start_rdist + self.rdist(dt)

        self.pid["L"].setSetpoint(lset)
        self.pid["R"].setSetpoint(rset)

        wpilib.SmartDashboard.putData("L Distance PID", self.pid["L"])
        wpilib.SmartDashboard.putData("R Distance PID", self.pid["R"])

    def end(self):
        self.applyPID(lambda pid: pid.disable())

    def isFinished(self):
        return time.time() - self.start_time >= self.timeout

    def interrupted(self):
        self.end()
