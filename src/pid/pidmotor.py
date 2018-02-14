from wpilib.interfaces.pidsource import PIDSource
from wpilib.interfaces.pidoutput import PIDOutput
from wpilib.encoder import Encoder


class PIDMotorSource(PIDSource):
    def __init__(self, _encoder):

        self.sourceType = Encoder.PIDSourceType.kRate
        self.encoder = _encoder
        self.encoder.setSamplesToAverage(16)
        self.scale = 1.0
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
        for motor in self.motors:
            speed = speed * self.scale
            motor.pidWrite(speed)
