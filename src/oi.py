"""

operator interface

"""

import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton


joystick_dictionary = { }

def get_joystick():
    return joystick_dictionary[0]


def init():
    global joystick_dictionary

    joystick_dictionary[0] = Joystick(0)

