import wpilib
from wpilib.command.subsystem import Subsystem

from hardware.solenoid import SolenoidHandler
from hardware.motor import Motor
from hardware.encoder import Encoder

from robotmap import extra_motors, solenoids

from puremath import Vector2D

class Arm(Subsystem):
    """

    This should hold motors, and all things related to the arm movement
    
    """

    def __init__(self):

        super().__init__("Arm")
        
        self.extender_solenoid = SolenoidHandler(*solenoids.armextender)
        self.grabber_solenoid = SolenoidHandler(*solenoids.grabber)

        self.rotator_motor = Motor(*extra_motors.arm_rotator)

    def set_extender(self, status):
        self.extender_solenoid.set(status)

    def set_grabber(self, status):
        self.grabber_solenoid.set(status)

    def set_rotator(self, amount):
        self.rotator_motor.set(amount)

    def grabber_position(self):
        """

        returns a Vector2D of grabber position

        res = Vector2D.from_polar(ARM_STAGE1_LENGTH, inclinometer.angle())

        if extended:
            res.radius += ARM_STAGE2_LENGTH

        """

        raise NotImplementedError()

    def stop_rotator(self):
        self.rotator_motor.set(0.0)





