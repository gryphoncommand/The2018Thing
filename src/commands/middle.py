import wpilib
from wpilib.command import CommandGroup
from commands.drivedist import DriveToDistance
from commands.turndrive import TurnDrive
# TODO: Add import statement for the DeliverCube Command.


class Middle(CommandGroup):
    def __init__(self, _direction):
        super().__init__("Middle")
        if _direction == True:
            # Left
            direction = 1
        else:
            # Right
            direction = -1

        # Drive Forward to the Scale, pass the Auto Line
        self.addSequential(DriveToDistance(10, 10, True))

        # Turn to the scale of based on the game data. TODO: Find the angle to turn to. 
        self.addSequential(TurnDrive(45*direction), 2.0)

        # Deliver the cube
        # self.addSequential( [Insert Deliver Cube method here.] )