import wpilib

from wpilib.command import CommandGroup
import subsystems
import math
import robotmap
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive

"""
class DriveTriangle(CommandGroup):
    def __init__(self, side1):
        super().__init__('DriveTriangle')
        side2 = side1 * math.sqrt(3)
        side3 = side1 * 2
        self.addSequential(DriveToDistance(side2, side2))
        self.addSequential(TurnDrive(150))
        self.addSequential(DriveToDistance(side3, side3))
        self.addSequential(TurnDrive(100))
        self.addSequential(DriveToDistance(side1, side1))
        self.addSequential(TurnDrive(90))

"""

class DriveTriangle(CommandGroup):
    def __init__(self, side1):
        super().__init__('DriveTriangle')

        for i in range(0, 4):
            self.addSequential(DriveToDistance(side1, side1))
            self.addSequential(TurnDrive(90))
            #self.addSequential(DriveToDistance(-side1, -side1))
        #self.addSequential(TurnDrive(90))
       # self.addSequential(TurnDrive(90))
       # self.addSequential(TurnDrive(90))


