from wpilib.interfaces.pidsource import PIDSource
from wpilib.interfaces.pidoutput import PIDOutput
from wpilib.encoder import Encoder


class PIDMotorSource(PIDSource):
    def __init__(self, _encoder):

        self.encoder = _encoder
        self.scale = 1.0

        # Currently, we are using kRate, although we may use kDisplacement in the future.
        # kRate gets us as close to the acutal speed as we can. 
        self.sourceType = Encoder.PIDSourceType.kRate
        self.encoder.setPIDSourceType(Encoder.PIDSourceType.kRate)

    def setScale(self, _scale):
        self.scale = _scale

    def useDistance(self):
        self.encoder.setPIDSourceType(Encoder.PIDSourceType.kDisplacement)
        self.sourceType = Encoder.PIDSourceType.kDisplacement

    def useSpeed(self):
        self.encoder.setPIDSourceType(Encoder.PIDSourceType.kRate)
        self.sourceType = Encoder.PIDSourceType.kRate

    def pidGet(self):
        if self.sourceType == Encoder.PIDSourceType.kDisplacement:
            return self.encoder.getDistance()
        elif self.sourceType == Encoder.PIDSourceType.kRate:
            return self.encoder.getRate()
        else:
            print("What the heck are you doing? [Encoder Type Error]" +
                  " Not Valid")
            return 0

    def getPIDSourceType(self):
        return self.sourceType


class PIDMotorOutput(PIDOutput):
    def __init__(self, _motors):
        self.motors = _motors
        self.scale = 1.0

    def setScale(self, _scale):
        self.scale = _scale
    
    def pidWrite(self, speed):
        if len(self.motors) > 1:
            self.motors[0].pidWrite(speed)
            self.motors[1].pidWrite(speed)
        elif len(self.motors) == 1:
            self.motors.pidWrite(speed)
        else:
            raise TypeError("Your motor parameter does not meet the length requirements (1 or 2) of the robot.")

