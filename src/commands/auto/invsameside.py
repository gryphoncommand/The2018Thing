import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
#from commands.runintake import RunIntake
from commands.grabber import Grabber
#from robotmap import 
# TODO: Add import statement for the DriveToCube and DeliverCube Command.

from robotmap import measures, auto_measures, inches, waits

"""

Inverse Same side means the Switch is on our side

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
    def __init__(self, direction):
        super().__init__("InvSameSide")
        self.direction = direction

        from commands.auto import Direction
        
        if direction == Direction.MIDDLE:
            print ("warning, passed Direction.MIDDLE to a side command, doing nothing")
            return

        # Drive Forward 10 ft

        end_point = auto_measures.to_switch
        
        
        self.addSequential(DriveToDistance(
            end_point,
            end_point
        ), 3.5)

        # drive then turn absed on direction

        # Turn Slightly towards goal. NOTE: Look into raising arm before you get to the scale.
        if direction == Direction.LEFT:
            self.addSequential(DoNothing(waits.turn))

            self.addSequential(TurnDrive(90), 1.2)
            
        elif direction == Direction.RIGHT:
            self.addSequential(DoNothing(waits.turn))

            self.addSequential(TurnDrive(-90), 1.2)

        # self.addParallel(LiftToProportion(measures.ROBOT_ARM_SWITCH_DROP), 1.5)

        self.addSequential(DriveToDistance(inches(20) + auto_measures.robot_starting_offset, inches(20) + auto_measures.robot_starting_offset), 3.5)

        # drop the cube
        #self.addSequential(RunIntake(1.0), 1.0)
            