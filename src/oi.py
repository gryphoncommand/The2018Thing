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
    
    geardown = JoystickButton(joystick, buttons.L_BUMPER)
    gearup = JoystickButton(joystick, buttons.R_BUMPER)
    grabberclose = JoystickButton(joystick, buttons.X)
    grabberopen = JoystickButton(joystick, buttons.SQUARE)
    

    geardown.whenPressed(GearShift(Gearing.LOW))
    gearup.whenPressed(GearShift(Gearing.HIGH))
    grabberclose.whenPressed(Grabber(True))
    grabberopen.whenPressed(Grabber(False))

