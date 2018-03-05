
import wpilib
from wpilib.interfaces.pidsource import PIDSource
from networktables import NetworkTables
import subsystems


class BoxNTPIDSource(PIDSource):
    def __init__(self, center_x_key, dft=None):
        self.center_x_key = center_x_key
        self.dft = dft

    def pidGet(self):
        center_x = subsystems.smartdashboard.getNumber(self.center_x_key)
        if center_x < 0 and self.dft is not None:
            center_x = self.dft
        return center_x




import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing, measures
from networktables import NetworkTables


'''
PARAMS:
The distance is in meters.
Remember
1 meter = 3.28084 feet.
1 meter = 39.3701 inches.
PID Source
PID Output
'''


class MoveToBox(Command):
    def __init__(self, default_turn="left"):
        super().__init__('MoveToBox')


        dft = 0.0

        if default_turn.lower() in ("r", "right"):
            dft = 1.0

        # PIDSource Init
        src = BoxNTPIDSource("center_x", dft)

        self.avg_lr_pow = .5
        self.lr_amp_diff = .3

        def output(pid_write):
            # pid_write is in (-1, 1)
            lpow = self.avg_lr_pow + pid_write * self.lr_amp_diff
            rpow = self.avg_lr_pow - pid_write * self.lr_amp_diff

            subsystems.tankdrive.set(lpow, rpow)


        self.PID = PIDController(
            pid.L[0], pid.L[1], pid.L[2], pid.L[3], 
            src,
            output
        )

        self.PID.setInputRange(0, 1)
        self.PID.setOutputRange(-1, 1)
        self.PID.setContinuous(False)

        self.PID.setAbsoluteTolerance(0.0)

    def initialize(self):
        subsystems.tankdrive.set_gearing(Gearing.LOW)
        self.PID.enable()
        self.PID.setSetpoint(0.5)

    def execute(self):
        wpilib.SmartDashboard.putData("Vision PID", self.PID)
        #if self.PID.onTarget():
        #    self.end()

    def end(self):
        self.PID.disable()

    def isFinished(self):
        #return self.PID.onTarget()
        # in pixels
        rad = subsystems.smartdashboard.getNumber("radius", 0)

        return rad >= 0 and rad < measures.ROBOT_CUBE_DISTANCE_CUTOFF

    def interrupted(self):
        self.end()


        

