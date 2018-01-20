from wpilib.encoder import Encoder

class MotorEncoder(Encoder):
    '''
    A class that serves as a hub for our encoders

    TO DO:
        Test the distance per tick by going a set amount of distance and finding the amount of ticks it returns.
    '''


    def __init__(self, channels):
        super().__init__(channels[0], channels[1], False, Encoder.EncodingType.k4X)

        if len(channels) != 2:
            print("Bruh, you incorrectly input the parameters for the encoder. ")