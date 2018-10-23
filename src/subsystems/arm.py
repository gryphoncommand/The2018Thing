import wpilib

from wpilib.command.subsystem import Subsystem
from hardware.solenoid import SolenoidHandler
from hardware.motor import Motor
from robotmap import arm_motors, arm_encoders, solenoids


class Arm(Subsystem):
    def __init__(self):
        super().__init__('Arm')

        self.extender_solenoid = SolenoidHandler(*solenoids.armextender)
        self.grabber_solenoid = SolenoidHandler(*solenoids.grabber)

        self.rotator_motors = {}
        self.rotator_motors["L"] = Motor(*arm_motors.L)
        self.rotator_motors["R"] = Motor(*arm_motors.R)

    def set_rotator(self, amount):
        for rot_mot in self.rotator_motors:
            self.rotator_motors[rot_mot].set(amount)

    def stop_rotator(self):
        self.set_rotator(0.0)

    def set_extender(self, status):
        self.extender_solenoid.set(status)

    def set_shooter(self, status):
        self.grabber_solenoid.set(status)
        