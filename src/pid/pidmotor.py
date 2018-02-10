from wpilib.interfaces.pidsource import PIDSource
from wpilib.interfaces.pidoutput import PIDOutput
from wpilib.encoder import Encoder
import subsystems
from robotmap import drive_encoders


class PIDMotorSource(PIDSource):
    def __init__(self, _encoder, _scalar1, _scalar2):
        self.scalar1 = _scalar1
        self.scalar2 = _scalar2
        self.sourceType = Encoder.PIDSourceType.kRate
        self.encoder = _encoder
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
            if self.encoder.getRate() > 0 and subsystems.tankdrive.gearshift.get() == True:
                return self.encoder.getRate() / self.scalar1[1]
            elif self.encoder.getRate() < 0 and subsystems.tankdrive.gearshift.get() == True:
                return self.encoder.getRate() / self.scalar1[0]
            elif self.encoder.getRate() > 0 and subsystems.tankdrive.gearshift.get() == False:
                return self.encoder.getRate() / self.scalar2[1]
            elif self.encoder.getRate() < 0 and subsystems.tankdrive.gearshift.get() == False:
                return self.encoder.getRate() / self.scalar2[0]
            else: 
                return self.encoder.getRate()        
        else:
            raise TypeError("Invalid Encoder PIDSourceType")
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
