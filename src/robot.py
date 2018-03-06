#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot
from wpilib.driverstation import DriverStation

import oi
import subsystems

import robotmap


import math


from commands.dumpinfo import DumpInfo
from commands.parametricdrive import ParametricDrive

from commands.pulsemotor import PulseMotor
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.left_pos import Left_POS
from commands.auto.right_pos import Right_POS
from commands.auto.middle import Middle
from commands.auto.donothing import DoNothing

from commands.sequence import Sequence

from commands.tankdrivejoystick import TankDriveJoystick
from commands.pidtankdrive import PIDTankDriveJoystick
from commands.armextender import ArmExtender
from commands.armrotate import ArmRotate

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

        self.chooser.addDefault("SEQUENCE", Sequence())
        self.chooser.addObject("Go 1 meter forward", DriveToDistance(1, 1))
        self.chooser.addObject("Turn 90 Degrees Clockwise", TurnDrive(90))
        self.chooser.addObject("Do Nothing Auto", DoNothing(15))

        #self.chooser.addObject("ParametricLine", ParametricDrive(lambda t: .1 * t, lambda t: .4 * t, 5))

        # The Auto Line is 10 ft (~3.048 meters) from the start point. May have to be tweaked a bit. 
        self.chooser.addObject("Drive Forward", DriveToDistance(3.048, 3.048))
        self.poschooser = wpilib.SendableChooser()
        self.poschooser.addObject("Left", "l")
        self.poschooser.addObject("Middle", "m")
        self.poschooser.addObject("Right", "r")
        self.poschooser.addObject("Do Nothing", "dn")
        self.poschooser.addObject("Minimal Auto", "min")
        


        #self.chooser.addObject('PulseMotor', PulseMotor())

        wpilib.SmartDashboard.putData('Autonomous Program', self.chooser)
        wpilib.SmartDashboard.putData('Auto', self.poschooser)

        self.teleopProgram = wpilib.command.CommandGroup()

        self.teleopProgram.addParallel(PIDTankDriveJoystick())
        #self.teleopProgram.addParallel(TankDriveJoystick())
        self.teleopProgram.addParallel(ArmExtender())
        self.teleopProgram.addParallel(ArmRotate())
        self.teleopProgram.addParallel(DumpInfo())
        #self.teleopProgram.addParallel(NavXCommand())
        #self.teleopProgram.addParallel(CorrectTip())

        oi.init()

    def autonomousInit(self):
        choice = self.poschooser.getSelected()
        data = DriverStation.getInstance().getGameSpecificMessage()
        if data is not None:
            datas = list(data)
            if choice == "l":
                self.autonomousProgram = Left_POS(data)
            elif choice == "m":
                self.autonomousProgram = Middle(datas[0] == "L")
            elif choice == "r":
                self.autonomousProgram = Right_POS(data)
            elif choice == "min":
                self.autonomousProgram = DriveToDistance(3.048, 3.048)
            else: 
                self.autonomousProgram = DoNothing(15)
        else:
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
