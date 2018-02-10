#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot

import oi
import subsystems

from commands.record import Record
from commands.playback import Playback


from commands.dumpinfo import DumpInfo

from commands.pulsemotor import PulseMotor

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
        self.teleopProgram = wpilib.command.CommandGroup()

        self.teleopProgram.addParallel(TankDriveJoystick())
        self.teleopProgram.addParallel(ArmExtender())
        self.teleopProgram.addParallel(ArmRotate())
        self.teleopProgram.addParallel(DumpInfo())
        # self.teleopProgram.addParallel(NavXCommand())
        #self.teleopProgram.addParallel(CorrectTip())

        #self.teleopProgram = Record(filename="macro_0.csv", concurrent_command=TankDriveJoystick())
        #self.autonomousProgram = Playback(filename="macro_0.csv", concurrent_command=TankDriveJoystick())

        oi.init()

    def autonomousInit(self):
        self.autonomousProgram.start()

    def teleopInit(self):
        self.teleopProgram.start()


if __name__ == '__main__':
    wpilib.run(The2018Thing)
