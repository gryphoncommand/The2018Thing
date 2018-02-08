from wpilib.encoder import Encoder

'''
    A class that serves as a hub for our encoders

    Created on 1-20-2018 by Tyler Duckworth
    TO DO:
        Test the distance per tick by going a set amount of distance and
        finding the amount of ticks it returns.
'''


class Encoders():

    def __init__(self, dio_in, dio_out, inverted=False):
        self.enc = Encoder(dio_in, dio_out, False,
                           Encoder.EncodingType.k4X)

    # returns the number of ticks.
    def get(self):
        return self.enc.get()
    
    def reset(self):
        self.enc.reset()

    '''
    # Class for the rate of the Encoder
    Requires setDistancePerTick
    def findRate(self):
        self.enc.getRate()
    '''
    def setPIDSourceType(self, sourceType):
        if sourceType == Encoder.PIDSourceType.kDisplacement:
            self.enc.setPIDSourceType(sourceType)
        elif sourceType == Encoder.PIDSourceType.kRate:
            self.enc.setPIDSourceType(sourceType)
        else:
            print("[Invalid Encoder PID Type given]")
            return 0
    
    def getRate(self):
        if self.enc.getPIDSourceType() == Encoder.PIDSourceType.kRate:
            return self.enc.getRate()
        else:
            raise TypeError("Invalid or Incorrect PID Type")

    def getDisplacement(self):
        if self.enc.getPIDSourceType() == Encoder.PIDSourceType.kDisplacement:
            return self.enc.getDistance()
        else:
            raise TypeError("Invalid or Incorrect PID Type")
