#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot

import oi
import subsystems

import robotmap


import math


from commands.dumpinfo import DumpInfo
from commands.parametricdrive import ParametricDrive
from commands.pulsemotor import PulseMotor
from commands.drivedist import DriveToDistance
from commands.turndrive import TurnDrive
from commands.sequence import Sequence
from commands.tankdrivejoystick import TankDriveJoystick
from commands.pidtankdrive import PIDTankDriveJoystick
from commands.armextender import ArmExtender
from commands.armrotate import ArmRotate
from commands.donothing import DoNothing
from commands.aligntobox import AlignToBox
from commands.shooter import Shooter


#from commands.correcttip import CorrectTip


#from commands.crash import Crash


get_robot = None


class The2018Thing(CommandBasedRobot):

    def get_self(self):
        """

        simple helper to get itself

        """
        return self

    def robotInit(self):
        """

        WPILIB method on initialization

        """

        # instansiate a getter method so you can do 'import robot;
        # robot.get_robot()'
        global get_robot
        get_robot = self.get_self

        subsystems.init()

        self.autonomousProgram = PulseMotor()

        self.chooser = wpilib.SendableChooser()

        self.chooser.addDefault("SEQUENCE", Sequence())
        self.chooser.addObject("Go 1 meter forward", DriveToDistance(1, 1))
        self.chooser.addObject("Turn 90 Degrees Clockwise", TurnDrive(90))
        self.chooser.addObject("Do Nothing Auto", DoNothing(15))
        self.chooser.addObject("Minimal Auto", DriveToDistance(3.048, 3.048))
        self.chooser.addObject("Align To Box", AlignToBox())

        

        _circle_radius = 3.0353 / 2.0
        _inner_radius = robotmap.measures.ROBOT_WHEELTOWHEEL_WIDTH / 2.0

        def ldist(t):
#            return t * 2
            ratio = _circle_radius - _inner_radius
            return (t / 4.0) * ratio
            #return 2 * math.pi * (_circle_radius - _inner_radius) * t / (12 * 360)
        def rdist(t):
            ratio = _circle_radius + _inner_radius
            return (t / 4.0) * ratio
            #return  * t / (12 * 360)

        self.chooser.addObject("ParametricCircle", ParametricDrive(ldist, rdist, 26))

        # The Auto Line is 10 ft (~3.048 meters) from the start point. May have to be tweaked a bit. 
        self.chooser.addObject("Drive Forward", DriveToDistance(3.048, 3.048))



        #self.chooser.addObject('PulseMotor', PulseMotor())

        wpilib.SmartDashboard.putData('Autonomous Program', self.chooser)

        self.teleopProgram = wpilib.command.CommandGroup()

        # self.teleopProgram.addParallel(PIDTankDriveJoystick())
        self.teleopProgram.addParallel(TankDriveJoystick())
        self.teleopProgram.addParallel(ArmExtender())
        self.teleopProgram.addParallel(ArmRotate())
        self.teleopProgram.addParallel(DumpInfo())
        #self.teleopProgram.addParallel(NavXCommand())
        #self.teleopProgram.addParallel(CorrectTip())

        oi.init()
        print("Robot Init Finished... Epic!!!")

    def autonomousInit(self):
        self.autonomousProgram = self.chooser.getSelected()
        #self.autonomousProgram = wpilib.command.CommandGroup()
        #self.autonomousProgram.addParallel(self.chooser.getSelected())
        #self.autonomousProgram.addParallel(DumpInfo())

        if self.autonomousProgram is not None:
            self.autonomousProgram.start()

    def teleopInit(self):
        self.teleopProgram.start()

if __name__ == '__main__':
    wpilib.run(The2018Thing)
