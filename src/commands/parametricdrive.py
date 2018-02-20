
import time

import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing, measures

import math
from puremath import Vector2D

class ParametricDrive(Command):
    def __init__(self, xpos, ypos, timeout):
        super().__init__('ParametricDrive')

        # these should be lambda t: t, and xpos(t), ypos(t) is where to robot will be
        self.xpos = xpos
        self.ypos = ypos

        self.timeout = timeout

        self.pid = {}
        self.pid["L"] = PIDController(pid.dist_L[0], pid.dist_L[1], pid.dist_L[2], pid.dist_L[3], subsystems.tankdrive.encoders["L"], subsystems.tankdrive.set_left)
        self.pid["R"] = PIDController(pid.dist_R[0], pid.dist_R[1], pid.dist_R[2], pid.dist_R[3], subsystems.tankdrive.encoders["R"], subsystems.tankdrive.set_right)

        self.applyPID(lambda p: p.setInputRange(-10**8, 10**8))
        self.applyPID(lambda p: p.setOutputRange(-1, 1))
        self.applyPID(lambda p: p.setContinuous(False))
        #self.applyPID(lambda p: p.useDistance())
        self.applyPID(lambda p: p.setPIDSourceType(PIDController.PIDSourceType.kDisplacement))
        self.applyPID(lambda p: p.setAbsoluteTolerance(.03))

        
    def applyPID(self, func):
        func(self.pid["L"])
        func(self.pid["R"])

    def initialize(self):
        subsystems.tankdrive.set_gearing(Gearing.LOW)

        self.start_time = time.time()

        #self.x_0 = subsystems.tankdrive.encoders["L"].getDistance()
        #self.y_0 = subsystems.tankdrive.encoders["R"].getDistance()

        self.l_start = subsystems.tankdrive.encoders["L"].getDistance()
        self.r_start = subsystems.tankdrive.encoders["R"].getDistance()

        self.l_dist = 0.0
        self.r_dist = 0.0

        self.last_lwheel_pos = Vector2D(0.0, 0.0)
        self.last_rwheel_pos = Vector2D(0.0, 0.0)
        self.last_pos = Vector2D(0.0, 0.0)

        self.pid["L"].setSetpoint(self.l_start)
        self.pid["R"].setSetpoint(self.r_start)

        self.applyPID(lambda pid: pid.enable())
        

    def execute(self):
        t = time.time() - self.start_time
        pos = Vector2D(self.xpos(self.t), self.ypos(self.t))

        dpos = pos - self.pos

        wheel_offset = Vector2D.from_polar(radius=measures.ROBOT_WHEELTOWHEEL_WIDTH / 2.0, angle=dpos.angle + math.pi / 2.0)

        self.pos = pos

        """

        dt = self.t - self.last_t
        dpos = self.pos - self.last_pos

        angle = dpos.get_angle(degress=True)

        # left wheel position, since the wheels are on the side
        wheel_offset = Vector2D.from_polar(radius=robotmap.measures.ROBOT_WHEELTOWHEEL_WIDTH / 2.0, angle=angle + 90, degrees=True)

        l_wheel_pos = pos + wheel_offset
        r_wheel_pos = pos - wheel_offset

        d_l_wheel_pos = l_wheel_pos - self.last_l_wheel_pos
        d_r_wheel_pos = r_wheel_pos - self.last_r_wheel_pos

        self.l_dist += d_l_wheel_pos.rotate(angle - self.last_angle).y
        self.r_dist += d_r_wheel_pos.rotate(angle - self.last_angle).y

        #instant_angle = math.atan2(dy, dx)
        #instant_speed = math.hypot(dx, dy)

        #instant_vec = Vector2D.from_polar(instant_speed, instant_angle)

        #math.cos(instant_angle) * instant_speed
        """

        #self.pid["L"].setSetpoint(self.l_start + self.t * .1)
        #self.pid["R"].setSetpoint(self.r_start + self.t * .1)

        """
        self.last_t = t

        self.last_l_wheel_pos = l_wheel_pos
        self.last_r_wheel_pos = r_wheel_pos

        self.last_pos = self.pos.copy()

        self.last_angle = angle

        """

        #wpilib.SmartDashboard.putData("L Distance PID", self.pid["L"])
        #wpilib.SmartDashboard.putData("R Distance PID", self.pid["R"])

    def end(self):
        self.applyPID(lambda pid: pid.disable())

    def isFinished(self):
        return time.time() - self.start_time >= self.timeout

    def interrupted(self):
        self.end()
