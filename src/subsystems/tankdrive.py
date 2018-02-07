import wpilib

from wpilib.command.subsystem import Subsystem
from wpilib import PIDController

from hardware.motor import Motor
from hardware.solenoid import SolenoidHandler
from hardware.encoder import Encoders

from commands.tankdrivejoystick import TankDriveJoystick

from robotmap import drive_motors, drive_encoders, solenoids, pid_controllers
from robotmap import Gearing

from puremath.scaling import transform

from enum import Enum


class TankDrive(Subsystem):
    """

    This example subsystem controls a single CAN Talon SRX in PercentVBus mode.
    
    Edit on 1-20-2018: Future Encoder code is commented out. Added Solenoid objects for gearshifting
    
    """

    def __init__(self, use_encoders=False):

        super().__init__("TankDrive")

        self.use_encoders = True

        self.motors = {
            "LF": Motor(*drive_motors.LF),
            "LB": Motor(*drive_motors.LB),
            "RF": Motor(*drive_motors.RF),
            "RB": Motor(*drive_motors.RB)
        }

        self.gearshift = SolenoidHandler(*solenoids.gearshift)

        if self.use_encoders:
            self.encoders = {
                "L": Encoders(*drive_encoders.L),
                "R": Encoders(*drive_encoders.R),
                "range": drive_encoders.lowgear_range
            }

            def get_drive_pid(t):
                pid = pid_controllers.drive
                ret = None
                if t == "L":
                    ret = PIDController(pid[0], pid[1], pid[2], self.encoders["L"].get, self.set_left)
                elif t == "R":
                    ret = PIDController(pid[0], pid[1], pid[2], self.encoders["R"].get, self.set_right)
                else:
                    raise Exception()
                # input from controllers should be from -1.0 to +1.0
                return ret

            self.pid = {
                "L": get_drive_pid("L"),
                "R": get_drive_pid("R"),
            }

            '''
            self.apply_to_pid(lambda pid: pid.setInputRange(*drive_encoders.lowgear_range))
            self.apply_to_pid(lambda pid: pid.setOutputRange(-1.0, 1.0))
            self.apply_to_pid(lambda pid: pid.setPIDSourceType(PIDController.PIDSourceType.kRate))
            '''

    def apply_to_pid(self, func):
        """

        apply to both pids (to avoid duplicated code)

        """
        if self.use_encoders:
            func(self.pid["L"])
            func(self.pid["R"])

    def set_left(self, power):
        self.motors["LF"].set(power)
        self.motors["LB"].set(power)
    
    def set_right(self, power):
        self.motors["RF"].set(power)
        self.motors["RB"].set(power)

    def set_power(self, Lpower=0, Rpower=None):
        if Rpower is None:
            # by default drive forward
            Rpower = Lpower

        self.set_left(Lpower)
        self.set_right(Rpower)

    def set(self, left, right):
        if self.use_encoders:
            # left_t = transform(left, (-1, 1), self.pid["range"])
            # right_t = transform(right, (-1, 1), self.pid["range"])
            # self.pid["L"].setSetpoint(left_t)
            # self.pid["R"].setSetpoint(right_t)
            self.set_power(left, right)
        else:
            self.set_power(left, right)


    def get_gearing(self):
        get = self.gearshift.get()
        if get == False:
            return Gearing.LOW
        elif get == True:
            return Gearing.HIGH
        else:
            raise Exception("internal problem calculating gearing")

    def set_gearing(self, gear):
        if gear == Gearing.LOW:
            self.gearshift.set(False)
            self.apply_to_pid(lambda pid: pid.setInputRange(*drive_encoders.lowgear_range))
            if self.use_encoders:
                self.pid["range"] = drive_encoders.lowgear_range

        elif gear == Gearing.HIGH:
            self.gearshift.set(True)
            self.apply_to_pid(lambda pid: pid.setInputRange(*drive_encoders.highgear_range))
            if self.use_encoders:
                self.pid["range"] = drive_encoders.highgear_range

        else:
            raise Exception("setting gearing to unknown gear")

