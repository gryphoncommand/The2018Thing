import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
# TODO: Add import statement for the DriveToCube and DeliverCube Command.

"""
Route Approximation:
            -----> Cube
            |
            |
            --> Close Scale
            |  
            |   
            |
        Startpoint
"""


class InvSameSide(CommandGroup):
    def __init__(self, _direction):
        super().__init__("InvSameSide")
        if _direction == True:
            # Left
            direction = 1
        else:
            # Right
            direction = -1
        
        # Drive Forward 10 ft
        self.addSequential(DriveToDistance(10, 10, True))

        # Turn 90 degrees to the scale. NOTE: Look into raising arm before you get to the scale.
        self.addSequential(TurnDrive(90*direction), 2.0)

        # Raise Arm and extend (Deliver Cube Method)
        # self.addSequential( [Imported Cube Delivery method] )

        # TODO: Refine Process of getting second cube
        # Move past scale TODO: Find this unit
        self.addSequential(DriveToDistance(5, 5, True))

        # Turn to cube 
        self.addSequential(TurnDrive(90*direction))

        # Move to Cube
        # self.addSequential( [Imported Cube Location function here] )
        # self.addSequential( [Imported Cube Delivery method] )
