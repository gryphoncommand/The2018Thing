"""

operator interface

"""

import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.gearshift import GearShift
from commands.grabber import Grabber
from commands.shooter import Shooter

from robotmap import Gearing

joystick = None

def init():
    global joystick
    joystick = Joystick(0)
    
    gearup = JoystickButton(joystick, 1)
    geardown = JoystickButton(joystick, 2)
    grabberclose = JoystickButton(joystick, 4)
    grabberopen = JoystickButton(joystick, 3)
    shooterdown = JoystickButton(joystick, 5)
    shooterup = JoystickButton(joystick, 6)
    # 5 and 6 are L and R bumpers

    gearup.whenPressed(GearShift(Gearing.HIGH))
    geardown.whenPressed(GearShift(Gearing.LOW))
    grabberclose.whenPressed(Grabber(True))
    grabberopen.whenPressed(Grabber(False))
    shooterup.whenPressed(Shooter(True))
    shooterdown.whenPressed(Shooter(False))

