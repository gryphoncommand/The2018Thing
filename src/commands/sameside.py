import wpilib
from wpilib.command import CommandGroup
from commands.drivedist import DriveToDistance
from commands.turndrive import TurnDrive
# TODO: Add import statement for the DriveToCube and DeliverCube Command.

"""
Route Approximation:
          Scale
          \   /
           \ /
            |\ 
            | \ 
            |  \ 
            |   Cube
            |
        Startpoint
"""


class SameSide(CommandGroup):
    def __init__(self, _direction):
        super().__init__("SameSide")
        if _direction == True:
            # Left
            direction = 1
        else:
            # Right
            direction = -1
        
        # Drive Forward 10 ft
        self.addSequential(DriveToDistance(10, 10, True))

        # Turn Slightly towards goal. NOTE: Look into raising arm before you get to the scale.
        self.addSequential(TurnDrive(45*direction), 2.0)

        # Raise Arm and extend (Deliver Cube Method)
        # self.addSequential( [Imported Cube Delivery method] )

        # Turn to cube TODO: Find this angle
        self.addSequential(TurnDrive(45*direction))

        # Move to Cube
        # self.addSequential( [Imported Cube Location function here] )
        # self.addSequential( [Imported Cube Delivery method] )
