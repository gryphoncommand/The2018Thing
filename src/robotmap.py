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

def feet(x):
    return x / FEET_PER_METER

def inches(x):
    return x / (12.0 * FEET_PER_METER)

auto_measures.green_tape = feet(10)

# Measures in meters
auto_measures.to_scale = inches(299.65)
auto_measures.to_switch = inches(140)
#auto_measures.to_cube = 1.542669

auto_measures.to_cubepyramid = feet(8)

auto_measures.from_middle_to_backofswitch = inches(32)
auto_measures.robot_middle_turn_dist = feet(3.0)


"""
b
|---- <- a (32 inches)
|  /
|A/ (60 degrees)
|/


a / b = tan(A)

b = a / tan(60)



"""

waits = InfoPasser()
# the wait time, in seconds, before you should start turning (small)
waits.turn = 0.2

"""

this is the offset that the robot is from the center (if on right or left)
So:

   [x]<---->|
------------|-------------

"""

# this is from the switch outside
auto_measures.robot_starting_offset = inches(14)

# Turn Measure in degrees
auto_measures.angle_scale = 42.5
auto_measures.angle_switch = 90
auto_measures.angle_cube = 135



#from robotmap_alpha import *
#from robotmap_beta import *

from robotmap_qbit import *


