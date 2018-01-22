import wpilib
from wpilib.command.subsystem import Subsystem
from hardware.motor import Motor
from hardware.solenoid import SolenoidHandler
from hardware.encoder import EncoderHandler

from robotmap import drive_motors, encoders, solenoids

class Arm(Subsystem):
    """

    This should hold motors, and all things related to the arm movement
    
    """

    def __init__(self):

        super().__init__("Arm")
        
        self.actuator = SolenoidHandler(*solenoids.arm)


    def set_grabber(self, actuator_status):
        self.actuator.set(actuator_status)
