"""

operator interface

"""

import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.gearshift import GearShift
from commands.grabber import Grabber

from robotmap import Gearing

joystick = None

def init():
    global joystick
    joystick = Joystick(0)
    
    gearup = JoystickButton(joystick, 5)
    geardown = JoystickButton(joystick, 6)
    grabberclose = JoystickButton(joystick, 4)
    grabberopen = JoystickButton(joystick, 3)
    

    gearup.whenPressed(GearShift(Gearing.HIGH))
    geardown.whenPressed(GearShift(Gearing.LOW))
    grabberclose.whenPressed(Grabber(True))
    grabberopen.whenPressed(Grabber(False))

