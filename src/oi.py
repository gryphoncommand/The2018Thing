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


def init():
    global joystick
    joystick = Joystick(0)
    

    JoystickButton(joystick, buttons.L_BUMPER).whenPressed(GearShift(Gearing.LOW))
    JoystickButton(joystick, buttons.R_BUMPER).whenPressed(GearShift(Gearing.HIGH))

    JoystickButton(joystick, buttons.X).whenPressed(Grabber("toggle"))


    #grabber_toggle_0.whenPressed(Grabber("toggle"))
    #grabberopen.whenPressed(Grabber(False))

