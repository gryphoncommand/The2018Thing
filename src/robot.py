#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot

import oi
import subsystems


from commands.tankdrivejoystick import TankDriveJoystick

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
        get_robot = get_self

        subsystems.init()
        #self.autonomousProgram = AutonomousProgram()
        self.teleopProgram = TankDriveJoystick()

        oi.init()


    def autonomousInit(self):
        pass
       # self.autonomousProgram.start()

    def teleopInit(self):
        self.teleopProgram.start()


if __name__ == '__main__':
    wpilib.run(The2018Thing)
