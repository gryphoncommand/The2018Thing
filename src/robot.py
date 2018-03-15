#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot
from wpilib.driverstation import DriverStation

import oi
import subsystems

import robotmap

import math

from commands.parametricdrive import ParametricDrive

from commands.pulsemotor import PulseMotor
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
from commands.lifttoproportion import LiftToProportion

from commands.grabber import Grabber

from commands.sequence import Sequence

from commands.tankdrivejoystick import TankDriveJoystick
from commands.pidtankdrive import PIDTankDriveJoystick
from commands.armextender import ArmExtender
from commands.armrotate import ArmRotate
import commands

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

        #self.chooser.addDefault("SEQUENCE", Sequence())

        self.chooser.addObject("Go 1 meter forward", DriveToDistance(1, 1))
        self.chooser.addObject("Turn 90 Degrees Clockwise", TurnDrive(90))
        self.chooser.addObject("Turn Arm Horizontal", LiftToProportion(robotmap.measures.ROBOT_ARM_HORIZONTAL))
        self.chooser.addObject("Do Nothing Auto", DoNothing(15))
        self.chooser.addObject("Grabber(True)", Grabber(True))
        self.chooser.addObject("Grabber(False)", Grabber(False))

        #self.chooser.addObject("ParametricLine", ParametricDrive(lambda t: .1 * t, lambda t: .4 * t, 5))

        # The Auto Line is 10 ft (~3.048 meters) from the start point. May have to be tweaked a bit. 
        self.chooser.addObject("Drive Forward", DriveToDistance(3.048, 3.048))

        self.chooser.addObject("COMP: Left", "l")
        self.chooser.addObject("COMP: Middle", "m")
        self.chooser.addObject("COMP: Right", "r")

        self.chooser.addDefault("COMP: Minimal Auto", DriveToDistance(3.048, 3.048))

        self.chooser.addObject("COMP: Do Nothing", DoNothing(15))
        

        #self.chooser.addObject('PulseMotor', PulseMotor())

        wpilib.SmartDashboard.putData('Autonomous Program', self.chooser)

        self.teleopProgram = wpilib.command.CommandGroup()

        self.teleopProgram.addParallel(PIDTankDriveJoystick())
        #self.teleopProgram.addParallel(TankDriveJoystick())

        self.teleopProgram.addParallel(ArmExtender())
        self.teleopProgram.addParallel(ArmRotate())

        #self.teleopProgram.addParallel(NavXCommand())
        #self.teleopProgram.addParallel(CorrectTip())

        oi.init()

    def autonomousInit(self):
        choice = self.chooser.getSelected()
        data = DriverStation.getInstance().getGameSpecificMessage()
        if data is not None:
            datas = list(data)
            if choice == "l":
                self.autonomousProgram = commands.auto.get_left_command(data)
            elif choice == "m":
                self.autonomousProgram = commands.auto.get_middle_command(data)
            elif choice == "r":
                print ("GETTING 'r' command, data: " + str(data))
                self.autonomousProgram = commands.auto.get_right_command(data)
            else:
                self.autonomousProgram = choice
        else:
            self.autonomousProgram = DoNothing(15)
        #self.autonomousProgram = wpilib.command.CommandGroup()
        #self.autonomousProgram.addParallel(self.chooser.getSelected())

        if self.autonomousProgram is not None:
            self.autonomousProgram.start()
    
    def teleopInit(self):
        self.teleopProgram.start()

    def teleopPeriodic(self):
        subsystems.dump_info()
        super().teleopPeriodic()
    
    def autonomousPeriodic(self):
        subsystems.dump_info()
        super().autonomousPeriodic()

    def disabledPeriodic(self):
        subsystems.dump_info()
        super().disabledPeriodic()
    
    def testPeriodic(self):
        subsystems.dump_info()
        super().testPeriodic()


if __name__ == '__main__':
    wpilib.run(The2018Thing)