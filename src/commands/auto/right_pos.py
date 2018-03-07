import wpilib
from wpilib.command import Command
import subsystems
from commands.auto.sameside import SameSide
from commands.auto.invsameside import InvSameSide
from commands.drivetodistance import DriveToDistance

def Right_POS(self, _data):
    data = list(_data)
    if data[1] == "L":
        return InvSameSide(False)
    elif data[1] == "R":
        return SameSide(False)
    else:
        return DriveToDistance(3.048, 3.048)
