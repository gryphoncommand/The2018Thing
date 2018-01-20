import wpilib
from wpilib.command import Command
import subsystems

'''
A module that holds the commands used to shift gears on the robots.
It contains some logic that calls on an object created in TankDrive.py

Created on 1-20-2018
Author: Tyler Duckworth
'''

class GearShiftUp(Command):
    def __init__(self):
        super().__init__("GearShiftUp")

    def initialize(self):
        self.isDone = False

    def execute(self):
        if subsystems.tankdrive.gearshift is not None:
            subsystems.tankdrive.gearshift.enable()
            self.isDone = True
        else:
            print("You are an idiot.")

    def isFinished(self):
        if self.isDone:
            return self.isDone
        else:
            print("You're not done!")
    def end(self):
        print("Fin")


class GearShiftDown(Command):
    def __init__(self):
        super().__init__("GearShiftDown")

    def initialize(self):
        self.isDone = False

    def execute(self):
        if subsystems.tankdrive.gearshift is not None:
            subsystems.tankdrive.gearshift.disable()
            self.isDone = True
        else:
            print("You are still a freaking idiot.")

    def isFinished(self):
        if self.isDone:
            return self.isDone
        else:
            print("You're not freaking done!")
    def end(self):
        print("Fin")
