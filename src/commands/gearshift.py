import wpilib
from wpilib.command import Command
import subsystems

'''
A module that holds the commands used to shift gears on the robots.
It contains some logic that calls on an object created in TankDrive.py

Created on 1-20-2018
Author: Tyler Duckworth
'''

class GearShift(Command):
    def __init__(self, solenoid_setting):
        super().__init__("GearShift")

        self.solenoid_setting = solenoid_setting

    def initialize(self):
        self.isDone = False

    def execute(self):
        if subsystems.tankdrive.gearshift is not None:
            subsystems.tankdrive.set_gearing(self.solenoid_setting)
        else:
            print ("warning: subsystems.tankdrive.gearshift is None!")
        self.isDone = True

    def isFinished(self):
        return self.isDone

