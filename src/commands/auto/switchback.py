import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
from commands.lifttoproportion import LiftToProportion
from commands.grabber import Grabber
import math
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



class SwitchBack_inplace(CommandGroup):
    def __init__(self):
        super().__init__("SwitchBack")
        self.addSequential(LiftToProportion(1.0))



class SwitchBack(CommandGroup):
    def __init__(self, direction, whereisgoal=None):
        super().__init__("SwitchBack")
        if whereisgoal is None:
            whereisgoal = direction
        self.direction = direction

        from commands.auto import Direction


        if direction == Direction.MIDDLE:
            start_turning = auto_measures.robot_middle_turn_dist + 0.15
            end_point = auto_measures.to_switch
            self.addSequential(DriveToDistance(start_turning, start_turning), 2.5)

            turn_angle = 23


            self.addSequential(DoNothing(waits.turn))

            if whereisgoal == Direction.LEFT:
                self.addSequential(TurnDrive(180 - turn_angle), 2.5)
            elif whereisgoal == Direction.RIGHT:
                self.addSequential(TurnDrive(-(180 - turn_angle)), 2.5)


            #self.addParallel(LiftToProportion(measures.ROBOT_ARM_SWITCH_DROP), 1.5)

            # should be (end_point - start_turning) * math.sec()
            hypot_dist = math.hypot((end_point - start_turning), math.tan(turn_angle * math.pi / 180.0) * (end_point - start_turning))

            self.addSequential(DriveToDistance(-hypot_dist, -hypot_dist), 2.6)
            
            #self.addSequential(Grabber(True))
            self.addSequential(LiftToProportion(1.0), 5)
            self.addSequential(LiftToProportion(-1.0))

        else:        
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

                self.addSequential(TurnDrive(-90), 1.2)
                
            elif direction == Direction.RIGHT:
                self.addSequential(DoNothing(waits.turn))

                self.addSequential(TurnDrive(90), 1.2)

            #self.addParallel(LiftToProportion(measures.ROBOT_ARM_SWITCH_DROP), 1.5)
            dist = inches(20) + auto_measures.robot_starting_offset
            self.addSequential(DriveToDistance(-dist,-dist), 2.5)

        # drop the cube
     #   self.addSequential(Grabber(True))
        self.addSequential(LiftToProportion(1.0), 5)
        self.addSequential(LiftToProportion(-1.0))

