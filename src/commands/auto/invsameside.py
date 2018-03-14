import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
from commands.lifttoproportion import LiftToProportion
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
        ))

        # drive then turn absed on direction

        # Turn Slightly towards goal. NOTE: Look into raising arm before you get to the scale.
        if direction == Direction.LEFT:
            self.addSequential(DoNothing(waits.turn))

            self.addSequential(TurnDrive(90), 1.0)

            self.addParallel(LiftToProportion(measures.ROBOT_ARM_SWITCH_DROP))

            self.addSequential(DriveToDistance(inches(20) + auto_measures.robot_starting_offset, inches(20) + auto_measures.robot_starting_offset), 4.0)
            # TODO: Deliver cube


            self.addSequential(Grabber(True))
            
        elif direction == Direction.RIGHT:
            self.addSequential(DoNothing(waits.turn))

            # turn towards the scale and then drive towards it
            self.addSequential(TurnDrive(-auto_measures.angle_scale), 2.0)
            #dist = math.hypot(end_point - start_turning_point, auto_measures.robot_starting_offset)
            #dist = math.hypot(end_point - start_turning_point, auto_measures.robot_starting_offset)
            dist = math.hypot(auto_measures.robot_starting_offset, (end_point - start_turning_point) * math.tan(auto_measures.angle_scale * math.pi / 180.0))
            self.addSequential(DriveToDistance(dist, dist))

            #self.addSequential(DoNothing(.5))
            # turn back to face it
            self.addSequential(DoNothing(waits.turn))
            
            self.addSequential(TurnDrive(auto_measures.angle_scale), 2.0)

            # TODO: deliver first cube
            self.addSequential(DoNothing(1))


            # SECOND CUBE HERE
            #self.addSequential(TurnDrive(180), 2.0)
            #self.addSequential(DriveToDistance(auto_measures.to_scale - auto_measures.to_switch, auto_measures.to_scale - auto_measures.to_switch))
            
