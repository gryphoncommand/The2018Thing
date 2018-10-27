"""

operator interface

"""

import wpilib

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.gearshift import GearShift
from commands.grabber import Grabber
from commands.shooter import Shooter

from robotmap import Gearing, buttons
from commands.armrotate import ArmRotate
joystick = None

rumble = False

def init():
    global joystick
    joystick = Joystick(0)
    

    # JoystickButton(joystick, buttons.L_BUMPER).whenPressed(GearShift(Gearing.LOW))
    # JoystickButton(joystick, buttons.R_BUMPER).whenPressed(GearShift(Gearing.HIGH))

    # #JoystickButton(joystick, buttons.SQUARE).whenPressed(Grabber(True))
    # JoystickButton(joystick, buttons.X).whenPressed(Grabber("toggle"))

    gearup = JoystickButton(joystick, 1)
    geardown = JoystickButton(joystick, 2)
    grabberclose = JoystickButton(joystick, 4)
    grabberopen = JoystickButton(joystick, 3)
    shooterdown = JoystickButton(joystick, 5)
    shooterup = JoystickButton(joystick, 6)
    homebutton = JoystickButton(joystick, 13)
    
    # 5 and 6 are L and R bumpers

    gearup.whenPressed(GearShift(Gearing.HIGH))
    geardown.whenPressed(GearShift(Gearing.LOW))
    grabberclose.whenPressed(Grabber(True))
    grabberopen.whenPressed(Grabber(False))
    shooterup.whenPressed(Shooter(True))
    shooterdown.whenPressed(Shooter(False))
    # homebutton.whenPressed(ArmRotate(True))

    #grabber_toggle_0.whenPressed(Grabber("toggle"))
    #grabberopen.whenPressed(Grabber(False))

def set_rumble():
    rumbl = not rumble
    if rumbl: 
        joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kLeftRumble, 1.0)
        joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kRightRumble, 1.0)
    else:
        joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kLeftRumble, 0.0)
        joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kRightRumble, 0.0)

    

