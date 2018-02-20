import wpilib
from wpilib.command.subsystem import Subsystem

from hardware.solenoid import SolenoidHandler
from hardware.motor import Motor
from hardware.encoder import Encoder

from wpilib import PIDController
from wpilib.pidcontroller import PIDController

from robotmap import arm_motors, arm_encoders, solenoids

from puremath import Vector2D

class Arm(Subsystem):
    """

    This should hold motors, and all things related to the arm movement
    
    """

    def __init__(self):

        super().__init__("Arm")
        
        self.final_extender_solenoid = SolenoidHandler(*solenoids.final_armextender)
        self.extender_solenoid = SolenoidHandler(*solenoids.armextender)
        self.grabber_solenoid = SolenoidHandler(*solenoids.grabber)
        
        self.rotator_motors = {}
        self.rotator_motors["L"] = Motor(*arm_motors.L)
        self.rotator_motors["R"] = Motor(*arm_motors.R)

        self.rotator_encoders = {}
        self.rotator_encoders["L"] = Encoder(*arm_encoders.L)
        self.rotator_encoders["R"] = Encoder(*arm_encoders.R)
        
        self.rotator_encoders["L"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        self.rotator_encoders["R"].setPIDSourceType(PIDController.PIDSourceType.kRate)


    def set_extender(self, status):
        self.extender_solenoid.set(status)

    def set_final_extender(self, status):
        self.final_extender_solenoid.set(status)

    def set_grabber(self, status):
        self.grabber_solenoid.set(status)

    def set_rotator(self, amount):
        for rot_mot in self.rotator_motors:
            self.rotator_motors[rot_mot].set(amount)


    def grabber_position(self):
        """

        returns a Vector2D of grabber position

        res = Vector2D.from_polar(ARM_STAGE1_LENGTH, inclinometer.angle())

        if extended:
            res.radius += ARM_STAGE2_LENGTH

        """

        raise NotImplementedError()

    def stop_rotator(self):
        self.set_rotator(0.0)






