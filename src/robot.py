#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot

import oi
import subsystems

from commands.record import Record
from commands.playback import Playback

from commands.tankdrivejoystick import TankDriveJoystick
from commands.pulsemotor import PulseMotor

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

        # instansiate a getter method so you can do 'import robot; robot.get_robot()'
        global get_robot
        get_robot = self.get_self


        subsystems.init()

        #self.autonomousProgram = PulseMotor()
        self.teleopProgram = TankDriveJoystick()

        #self.teleopProgram = Record(filename="macro_0.csv", concurrent_command=TankDriveJoystick())
        self.autonomousProgram = Playback(filename="macro_0.csv", concurrent_command=TankDriveJoystick())

        oi.init()
 

    def autonomousInit(self):
        self.autonomousProgram.start()

    def teleopInit(self):
        self.teleopProgram.start()
        subsystems.dump_info()


if __name__ == '__main__':
    wpilib.run(The2018Thing)
