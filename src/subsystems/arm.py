import wpilib
from wpilib.command.subsystem import Subsystem

from hardware.solenoid import SolenoidHandler
from hardware.motor import Motor
from hardware.encoder import Encoder

from commands.armrotate import ArmRotate_reset

from puremath.scaling import transform


from wpilib import PIDController
from wpilib.pidcontroller import PIDController

from robotmap import arm_motors, arm_encoders, solenoids, arm_stopper, measures

from puremath import Vector2D
from wpilib.digitalinput import DigitalInput

class Arm(Subsystem):
    """

    This should hold motors, and all things related to the arm movement
    
    """

    def __init__(self):

        super().__init__("Arm")

        self.limiter = DigitalInput(arm_stopper.dio)
        self.final_extender_solenoid = SolenoidHandler(*solenoids.final_armextender)
        self.extender_solenoid = SolenoidHandler(*solenoids.armextender)
        self.grabber_solenoid = SolenoidHandler(*solenoids.grabber)
        
        self.rotator_motors = {}
        self.rotator_motors["L"] = Motor(*arm_motors.L)
        self.rotator_motors["R"] = Motor(*arm_motors.R)

        self.rotator_encoders = {}
        #self.rotator_encoders["L"] = Encoder(*arm_encoders.L)
        self.rotator_encoders["R"] = Encoder(*arm_encoders.R)
        

        #self.rotator_encoders["L"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        self.rotator_encoders["R"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        self.rotator_encoders["R"].setDistancePerPulse(arm_encoders.R_dpp)


    def set_extender(self, status):
        self.extender_solenoid.set(status)

    def set_final_extender(self, status):
        self.final_extender_solenoid.set(status)

    def set_grabber(self, status):
        self.grabber_solenoid.set(status)

    def get_limiter(self):
        return self.limiter.get()

    def get_arm_angle(self):
        return transform(self.get_arm_proportion(), (0, 1), measures.ROBOT_ARM_ANGLE_RANGE)

    def get_arm_proportion(self):
        r_ticks = []
        for i in self.rotator_encoders.keys():
            r_ticks += [self.rotator_encoders[i].getDistance()]
        
        return sum(r_ticks) / len(r_ticks)

    def set_rotator(self, amount, raw=True):
        if self.get_limiter() != arm_stopper.default:
            self.reset_enc()
        
        prop = self.get_arm_proportion()

        def envelope(x):
            # x is range -1 to +1
            p = prop
            if x > 1.0:
                x = 1.0
            elif x < -1.0:
                x = -1.0

            if p > 1.0:
                p = 1.0
            elif p < 0:
                p = 0


            lower_lim = .27
            upper_lim = .75

            if p < lower_lim:
                slope = .5 * p / lower_lim + .5
                return slope * x
            #elif p > upper_lim:
            elif p > upper_lim:
                slope = .36 * (upper_lim - p) / (1.0 - upper_lim) + .64
                return slope * x
            else:
                return x

            if p >= .25 and p <= .75:
                return x
            else:
                slope = 1.0 - .6 * (4 * (abs(p - .5) - .25))
                return x * slope

        if not raw:
            amount = envelope(amount)

        for rot_mot in self.rotator_motors:
            self.rotator_motors[rot_mot].set(amount)

    def reset_enc(self):
        for k in self.rotator_encoders.keys():
            self.rotator_encoders[k].reset()

    def grabber_position(self):
        """

        returns a Vector2D of grabber position

        res = Vector2D.from_polar(ARM_STAGE1_LENGTH, inclinometer.angle())

        if extended:
            res.radius += ARM_STAGE2_LENGTH

        """
        res = Vector2D.from_polar(ARM_STAGE1_LENGTH, inclinometer.angle())


        raise NotImplementedError()

    def stop_rotator(self):
        self.set_rotator(0.0)






