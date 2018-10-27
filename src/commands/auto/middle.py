import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
from commands.autoarmextender import AutoArmExtender
# from commands.lifttoproportion import LiftToProportion
from commands.grabber import Grabber

# TODO: Add import statement for the DriveToCube and DeliverCube Command.

from robotmap import measures, auto_measures, inches, waits
import math

class Middle(CommandGroup):
    def __init__(self, whereisgoal):
        super().__init__("Middle")

        from commands.auto import Direction

        # Drive Forward to the Scale, pass the Auto Line
        start_turning = auto_measures.robot_middle_turn_dist
        end_point = auto_measures.to_switch
        self.addSequential(DriveToDistance(start_turning, start_turning), 2.5)

        turn_angle = 45


        self.addSequential(DoNothing(waits.turn))

        if whereisgoal == Direction.LEFT:
            self.addSequential(TurnDrive(-turn_angle), 1.6)
        elif whereisgoal == Direction.RIGHT:
            self.addSequential(TurnDrive(turn_angle), 1.6)


        # self.addParallel(LiftToProportion(measures.ROBOT_ARM_SWITCH_DROP), 1.5)

        # should be (end_point - start_turning) * math.sec()
        hypot_dist = math.hypot((end_point - start_turning), math.tan(turn_angle * math.pi / 180.0) * (end_point - start_turning))

        self.addSequential(DriveToDistance(hypot_dist, hypot_dist), 2.4)
        
        self.addSequential(Grabber(True))


        # Turn to the scale of based on the game data. TODO: Find the angle to turn to. 
       # self.addSequential(TurnDrive(45*direction), 2.0)

        # Deliver the cube
        # self.addSequential( [Insert Deliver Cube method here.] )