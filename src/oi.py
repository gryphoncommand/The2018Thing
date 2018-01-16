"""

operator interface

"""

import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton


joystick_dictionary = { }

def get_joystick(key=0):
    """

    If key is an 

    """
    if key in joystick_dictionary:
        return joystick_dictionary[key]
    else:
        if isinstance(key, int):
            joystick_dictionary[key] = Joystick(key)
            return joystick_dictionary[key]
        else:
            raise KeyError("uknown joystick: %s" % key)



def init():
    pass
#    global joystick_dictionary
#    joystick_dictionary[0] = Joystick(0)

