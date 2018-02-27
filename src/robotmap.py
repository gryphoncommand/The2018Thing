"""

switch which robot

"""


from enum import Enum


# roboRIO IP address
roborio = "roborio-3966-frc.local"


class InfoPasser:
    """
    
    Dummy class used to store variables on an object.
    
    """
    pass


class NavXType(Enum):

    I2C = 1
    SPI = 2


class Gearing(Enum):
    """

    Enum gearing

    """

    LOW = 0
    HIGH = 1

buttons = InfoPasser()

buttons.X = 2
buttons.SQUARE = 1
buttons.L_BUMPER = 5
buttons.R_BUMPER = 6


from robotmap_alpha import *

#from robotmap_beta import *


