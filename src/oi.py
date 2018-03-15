"""

operator interface

"""

import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.gearshift import GearShift
from commands.grabber import Grabber

from robotmap import Gearing, buttons

joystick = None
assist_joystick = None


def init():
    global joystick; global assist_joystick
    joystick = Joystick(0)
    assist_joystick = Joystick(1)
    
    grabber_toggle_0 = JoystickButton(joystick, buttons.X)
    #grabberopen = JoystickButton(joystick, buttons.SQUARE)
    

    JoystickButton(joystick, buttons.L_BUMPER).whenPressed(GearShift(Gearing.LOW))
    JoystickButton(joystick, buttons.R_BUMPER).whenPressed(GearShift(Gearing.HIGH))

    JoystickButton(joystick, buttons.X).whenPressed(Grabber("toggle"))

    JoystickButton(assist_joystick, buttons.X).whenPressed(Grabber("toggle"))

    #grabber_toggle_0.whenPressed(Grabber("toggle"))
    #grabberopen.whenPressed(Grabber(False))

