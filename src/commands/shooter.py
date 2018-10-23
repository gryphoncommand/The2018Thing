import wpilib
from wpilib.command import Command
import subsystems

'''
A module that holds the commands used to activate/disable the solenoids on the robot's shooter.
It contains some logic that calls on an object created in TankDrive.py

Created on 10-16-2018
Author: Tyler Duckworth
'''


class Shooter(Command):
    def __init__(self, solenoid_setting):
        super().__init__("Shooter")

        self.solenoid_setting = solenoid_setting

    def initialize(self):
        self.isDone = False

    def execute(self):
        if subsystems.arm.grabber_solenoid is not None:
            subsystems.arm.set_grabber(self.solenoid_setting)
        else:
            print("warning: subsystems.tankdrive.shooter is None!")
        self.isDone = True

    def isFinished(self):
        return self.isDone
