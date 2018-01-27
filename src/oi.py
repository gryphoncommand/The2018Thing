"""

operator interface

"""

import wpilib

import recordplayback

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.gearshift import GearShift
from commands.grabber import Grabber

from robotmap import Gearing


joystick_dictionary = { }

joystick_source_hash = { }




# set_default_joystick(get_joystick("tankdrive.csv"))

def get_joystick(key=None, force=False):
    """

    If key is an 

    """
    if key is None:
        key = joystick_dictionary["default"]

    if key in joystick_dictionary and not force:
        if key in joystick_source_hash:
            full_path = recordplayback.macro_dir + key
            fp = open(full_path)
            file_contents = fp.read()
            fp.close()
            if hash(file_contents) != joystick_source_hash[key]:
                joystick_source_hash[key] = hash(file_contents)
                sampler = recordplayback.ControllerSamples(file_contents)
                joystick_dictionary[key] = recordplayback.MockController(sampler)
        return joystick_dictionary[key]
    else:
        if isinstance(key, int):
            print ('instansiate joystick %d' % key)
            joystick_dictionary[key] = Joystick(key)
            return joystick_dictionary[key]
        elif isinstance(key, str):
            ext = key.split(".")[-1]
            full_path = recordplayback.macro_dir + key
            fp = open(full_path)
            file_contents = fp.read()
            fp.close()
            joystick_source_hash[key] = hash(file_contents)
            sampler = recordplayback.ControllerSamples(file_contents)
            joystick_dictionary[key] = recordplayback.MockController(sampler)
            return joystick_dictionary[key]
        raise KeyError("uknown joystick: %s" % key)

def set_default_joystick_key(key):
    joystick_dictionary["default"] = key


def init():
    set_default_joystick_key(key=0)
    
    gearup = JoystickButton(get_joystick(), 5)
    geardown = JoystickButton(get_joystick(), 6)
    grabberclose = JoystickButton(get_joystick(), 4)
    grabberopen = JoystickButton(get_joystick(), 3)
    

    gearup.whenPressed(GearShift(Gearing.HIGH))
    geardown.whenPressed(GearShift(Gearing.LOW))
    grabberclose.whenPressed(Grabber(True))
    grabberopen.whenPressed(Grabber(False))

