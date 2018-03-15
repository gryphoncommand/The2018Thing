import wpilib
from wpilib.command import Command
import subsystems
from commands.auto.sameside import SameSide
from commands.auto.middle import Middle
from commands.auto.invsameside import InvSameSide
from commands.drivetodistance import DriveToDistance
from robotmap import auto_measures

from enum import Enum


class Direction(Enum):

    LEFT = 0
    MIDDLE = 1
    RIGHT = 2



def pass_green_tape():
    return DriveToDistance(auto_measures.green_tape + 0.25, auto_measures.green_tape + 0.25)


def get_left_command(data):
    data = data if data is None else list(data)
    if data is None or len(data) != 3:
        return pass_green_tape()
    else:
        if data[1] == "L":
            return SameSide(Direction.LEFT) 
        elif data[1] == "R" and data[0] == "L":
            return InvSameSide(Direction.LEFT)
        else:
            return pass_green_tape()

def get_middle_command(data):
    data = data if data is None else list(data)
    if data is None or len(data) != 3:
        return pass_green_tape()
    else:
        if data[0] == "L":
            return Middle(Direction.LEFT) 
        elif data[0] == "R":
            return Middle(Direction.RIGHT)
        else:
            return pass_green_tape()

def get_right_command(data):
    data = data if data is None else list(data)
    if data is None or len(data) != 3:
        return pass_green_tape()
    else:
        if data[1] == "R":
            return SameSide(Direction.RIGHT) 
        elif data[1] == "L" and data[0] == "R":
            return InvSameSide(Direction.RIGHT)
        else:
            return pass_green_tape()



