import wpilib

from wpilib.command.subsystem import Subsystem 
from hardware.navx import NavX
from robotmap import navx_type, solenoids


'''
A class for the various sensors on the robot. 
Currently includes Kauai Labs NavX.abs

Created on 1-20-2018 by Tyler Duckworth
'''

class Sensors(Subsystem):
    
    def __init__(self):
        super().__init__("Sensors")
        self.navx = NavX(navx_type)
        self.pressure_sensor = wpilib.AnalogInput(solenoids.pressure_sensor)
        # self.navx = None
        wpilib.LiveWindow.addSensor("Sensors", "PDP", wpilib.PowerDistributionPanel(0)) 




