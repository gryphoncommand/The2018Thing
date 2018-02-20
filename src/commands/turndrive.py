import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing
from pid.pidnavx import PIDNavXSource


class TurnDrive(Command):
    def __init__(self, _angle):
        super().__init__('TurnDrive')

        self.requires(subsystems.tankdrive)

        self.angle = _angle

        def set_opposite(pw):
            wpilib.SmartDashboard.putNumber("TurnDrive pidOutput", pw)
            subsystems.tankdrive.set_left(pw)
            subsystems.tankdrive.set_right(-pw)

        src = PIDNavXSource(subsystems.sensors.navx)

        #self.navx = PIDNavXSource(subsystems.sensors.navx)
        self.PID = PIDController(pid.angle[0], pid.angle[1], pid.angle[2], pid.angle[3], src, set_opposite)

        self.PID.setInputRange(-180.0, 180.0)
        self.PID.setOutputRange(-0.7, 0.7)
        self.PID.setContinuous(True)
        self.PID.setAbsoluteTolerance(2.5)

        self.PID.setPIDSourceType(PIDController.PIDSourceType.kDisplacement)

        self.PID.disable()


    def initialize(self):
        val = subsystems.sensors.navx.getYaw() + self.angle

        subsystems.tankdrive.set_gearing(Gearing.LOW)

        #print ("TURNDRIVE INITIALIZE[" + str(self.angle) + "] !!: " + str(val))

        while val > 180:
            val -= 360.0
        while val < -180:
            val += 360

        self.PID.setSetpoint(val)

        self.PID.enable()


    def execute(self):
        pass
        #if not self.is_init:
        #    self.initialize()#

        #    self.is_init = True

        #wpilib.SmartDashboard.putData("Angle PID", self.PID)
        #wpilib.SmartDashboard.putNumber("Angle PID Setpoint", self.val)
        #subsystems.dump_info()
        

    def end(self):
        self.PID.disable()
        #subsystems.tankdrive.stop()
        #self.is_init = False


    def isFinished(self):
        return self.PID.onTarget()
        #return self.is_init and self.PID.onTarget()
        #return False


    def interrupted(self):
        self.end()
