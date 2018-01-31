import wpilib
from wpilib.command import Command

import subsystems
import oi

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
    
    VARIABLES:
        isTipped = A boolean that tells whether or not the robot is tipped over.
        tipDir = An int that holds the value that classifies the tip.
            0 : Default; Stable
            1 : It is Tipped Forward
            2 : It is Tipped Backwards
'''

class NavXCommand(Command):

    def __init__(self):

        super().__init__("Tip Over")

    def initalize(self):

        self.isTipped = False
        self.tipDir = 0

    def execute(self):

        self.angle = subsystems.sensors.navx.getRoll()

        if self.angle > 45:
            print("WARNING: THE ROBOT IS TIPPING BACKWARDS \n MECHANISM FIRING NOW")
            self.tipDir = 2
            mechanism(True)
        elif self.angle < -45:
            print("WARNING: THE ROBOT IS TIPPING FORWARDS \n MECHANISM FIRING NOW")
            self.tipDir = 1
            mechanism(False)
        else: 
            self.tipDir = 0
            self.subsystems.tankdrive.set_power(0, 0)

    def mechanism(self, direction):
        if direction:
            self.subsystems.tankdrive.set_power(-1, -1)
        elif direction == False:
            self.subsystems.tankdrive.set_power(1, 1)
        else: 
            print("Whatcho talkin' bout Willis?")

    def end(self):
        pass

