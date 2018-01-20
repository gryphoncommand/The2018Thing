import wpilib

from wpilib.command.subsystem import Subsystem 
from robotpy_ext.common_drivers import navx

'''
A class for the various sensors on the robot. 
Currently includes Kauai Labs NavX.abs

Created on 1-20-2018 by Tyler Duckworth
'''

class Sensors(Subsystem):
    
    def __init__(self):
        self.NavX = navx.AHRS.create_spi()
    
    def navxGetYaw(self):
        return self.NavX.getBoardYawAxis()

    #Mr. Brown suggested the idea that we can see if the NavX displacement is a good backup.
    def navxGetDisp(self):
        return self.NavX.getDisplacementZ()
