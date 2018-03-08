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

auto_measures = InfoPasser()


FEET_PER_METER = 3.28084

def from_imp(ft=0, inches=0):
    return (ft + inches / 12.0) / FEET_PER_METER

def feet(x):
    return x / FEET_PER_METER

def inches(x):
    return x / (12.0 * FEET_PER_METER)

auto_measures.green_tape = feet(10)

# Measures in meters
auto_measures.to_scale = inches(299.65)
auto_measures.to_switch = inches(140)
#auto_measures.to_cube = 1.542669

"""

this is the offset that the robot is from the center (if on right or left)
So:

   [x]<---->|
------------|-------------

"""

# this is from the switch outside
auto_measures.robot_starting_offset = inches(18)

# Turn Measure in degrees
auto_measures.angle_scale = 45
auto_measures.angle_switch = 90
auto_measures.angle_cube = 135



from robotmap_alpha import *

#from robotmap_beta import *


