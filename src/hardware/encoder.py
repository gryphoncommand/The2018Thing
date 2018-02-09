from wpilib.encoder import Encoder

'''
    A class that serves as a hub for our encoders

    Created on 1-20-2018 by Tyler Duckworth
    TO DO:
        Test the distance per tick by going a set amount of distance and
        finding the amount of ticks it returns.
'''


class Encoders(Encoder):

    def __init__(self, dio_in, dio_out, inverted=False):
        super().__init__(dio_in, dio_out)
        self.setDistancePerPulse(1.0/2950)

    # returns the number of ticks.

    def restart(self):
        self.reset()

    '''
    # Class for the rate of the Encoder
    Requires setDistancePerTick
    def findRate(self):
        self.enc.getRate()
    '''
