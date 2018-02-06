from wpilib.interfaces.pidsource import PIDSource
from wpilib.interfaces.pidoutput import PIDOutput


class PIDMotorSource(PIDSource):
    def __init__(self, _encoder):

        self.sourceType = PIDSource.PIDSourceType.kRate
        self.encoder = _encoder
        self.scale = 1.0
        self.setPIDSourceType(sourceType)

    def setScale(self, _scale):
        self.scale = _scale

    def useDistance(self):
        self.setPIDSourceType(PIDSource.PIDSourceType.kDisplacement)
        self.sourceType = PIDSource.PIDSourceType.kDisplacement

    def useSpeed(self):
        self.setPIDSourceType(PIDSource.PIDSourceType.kRate)
        self.sourceType = PIDSource.PIDSourceType.kRate

    def pidGet(self):
        if self.sourceType == PIDSource.PIDSourceType.kDisplacement:
            return self.encoder.getDistance()
        elif self.sourceType == PIDSource.PIDSourceType.kRate:
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
            motor.pidWrite(self.speed * self.scale)
