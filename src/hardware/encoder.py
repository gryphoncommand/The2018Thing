from wpilib.encoder import Encoder

'''
    A class that serves as a hub for our encoders

    Created on 1-20-2018 by Tyler Duckworth
    TO DO:
        Test the distance per tick by going a set amount of distance and
        finding the amount of ticks it returns.
'''


class Encoder():

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
