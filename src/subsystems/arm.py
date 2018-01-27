import wpilib
from wpilib.command.subsystem import Subsystem
from hardware.motor import Motor
from hardware.solenoid import SolenoidHandler
from hardware.motor import Motor
from hardware.encoder import Encoder

from robotmap import drive_motors, extra_motors, encoders, solenoids

class Arm(Subsystem):
    """

    This should hold motors, and all things related to the arm movement
    
    """

    def __init__(self):

        super().__init__("Arm")
        
        self.extender = SolenoidHandler(*solenoids.armextender)
        self.grabber = SolenoidHandler(*solenoids.grabber)

        self.rotator = Motor(*extra_motors.arm_rotator)
