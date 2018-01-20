import wpilib
from networktables import NetworkTables 
from wpilib.smartdashboard import SmartDashboard
from wpilib.driverstation import DriverStation

'''
This class is a hub for the subsystems folder. It is mainly used to dump info to the SmartDashboard/ShuffleBoard

Created on 1-20-2018 by Tyler Duckworth
'''

class Subsystems():

    def __init__(self):
        self.isEnabled = True

        NetworkTables.setIPAdress(server="roborio-3966-frc.local")
        NetworkTables.setClientMode()
        NetworkTables.initialize()
        self.sd = NetworkTables.getTable('SmartDashboard')
        self.infoT = NetworkTables.getTable('info')
    
    #Method for dumping sensor info, encoders, etc

    def dumpInfo(self):
        #There is a way to create an instance of NetworkTables for SmartDashboard, but I chose to use the SmartDashboard module.
        SmartDashboard.PutData("Battery Voltage: ", DriverStation.getInstance().getBatteryVoltage())
