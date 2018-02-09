import wpilib
from wpilib.command import Command

import subsystems
import oi
import enum

'''
            Front

        z   x
        |  /
        | /
        |/_____ y

            Back
            
        Rudimentary axes map.


    A class made to detect whether or not the robot is tipped over. 
    The robot is considered 'tipped over' if it has an x axis rating above 45 degrees.
    It can be considered tippedForward if the angle is -45 degrees
    Vice versa for tippedBackward 
    

'''


class Direction(enum.Enum):

    NONE = 0
    FORWARD = 1
    BACKWARD = 2


class CorrectTip(Command):

    def __init__(self):

        super().__init__("CorrectTip")

    def initalize(self):

        self.isTipped = False
        self.tipDir = Direction.NONE
        self.last_tipDir = self.tipDir

    def execute(self):

        self.angle = subsystems.sensors.navx.getRoll()

        if self.angle > 45:
            print("WARNING: THE ROBOT IS TIPPING BACKWARDS \n MECHANISM FIRING NOW")
            self.tipDir = Direction.BACKWARD
        elif self.angle < -45:
            print("WARNING: THE ROBOT IS TIPPING FORWARDS \n MECHANISM FIRING NOW")
            self.tipDir = Direction.FORWARD
        else: 
            self.tipDir = Direction.NONE

        self.run_mechanism()
        self.last_tipDir = self.tipDir


    def run_mechanism(self):
        if self.tipDir == Direction.FORWARD:
            self.subsystems.tankdrive.set(-1, -1)
        elif self.tipDir == Direction.BACKWARD:
            self.subsystems.tankdrive.set(1, 1)
        elif self.last_tipDir != self.tipDir: 
            # only set it once so it doesn't control it over and over
            self.subsystems.tankdrive.set(0, 0)

    def end(self):
        pass

