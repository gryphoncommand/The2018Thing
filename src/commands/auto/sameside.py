import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
# TODO: Add import statement for the DriveToCube and DeliverCube Command.

from robotmap import auto_measures
import math

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
    def __init__(self, direction):
        super().__init__("SameSide")
        self.direction = direction
        # import it here
        from commands.auto import Direction
        print ("__init__ sameside")
        #if _direction:
            # Left
        #    direction = 1
        #else:
            # Right
        #    direction = -1
        
        if direction == Direction.MIDDLE:
            print ("warning, passed Direction.MIDDLE to a side command, doing nothing")
            return

        # Drive Forward 10 ft
        start_turning_point = (auto_measures.to_scale + auto_measures.to_switch)/2.0 - 0.25
        self.addSequential(DriveToDistance(
            start_turning_point, 
            start_turning_point
        ))

        # Turn Slightly towards goal. NOTE: Look into raising arm before you get to the scale.
        if direction == Direction.LEFT:
            self.addSequential(TurnDrive(auto_measures._scale), 2.0)
            dist = math.hypot(auto_measures.to_scale - start_turning_point, auto_measures.robot_starting_offset)
            self.addSequential(DriveToDistance(dist, dist))
            self.addSequential(TurnDrive(-auto_measures._scale), 2.0)
            # TODO: deliver cube
            self.addSequential(DoNothing(3))
            self.addSequential(TurnDrive(180), 2.0)
            self.addSequential(DriveToDistance(auto_measures.to_scale - auto_measures.to_switch, auto_measures.to_scale - auto_measures.to_switch))

            
        elif direction == Direction.RIGHT:
            self.addSequential(TurnDrive(-auto_measures._scale), 2.0)
            dist = math.hypot(auto_measures.to_scale - start_turning_point, auto_measures.robot_starting_offset)
            self.addSequential(DriveToDistance(dist, dist))
            self.addSequential(TurnDrive(auto_measures._scale), 2.0)
            # TODO: deliver cube
            self.addSequential(DoNothing(3))

            self.addSequential(TurnDrive(180), 2.0)
            self.addSequential(DriveToDistance(auto_measures.to_scale - auto_measures.to_switch, auto_measures.to_scale - auto_measures.to_switch))
            
            

        # Raise Arm and extend (Deliver Cube Method)
        # self.addSequential( [Imported Cube Delivery method] )

        # Turn to cube TODO: Find this 
        #if direction == Direction.LEFT:
        
        
        #self.addSequential(DoNothing(5))

        #self.addSequential(TurnDrive(90*direction))

        # Move to Cube
        # self.addSequential( [Imported Cube Location function here] )
        # self.addSequential( [Imported Cube Delivery method] )
