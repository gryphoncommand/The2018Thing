import wpilib
from wpilib.command.subsystem import Subsystem
from hardware.motor import Motor

from commands.tankdrivejoystick import TankDriveJoystick

from robotmap import drive_motors

class TankDrive(Subsystem):
    """

    This example subsystem controls a single CAN Talon SRX in PercentVBus mode.
    
    """

    def __init__(self):

        super().__init__("TankDrive")

        self.motors = {
            "LF": Motor(*drive_motors.LF),
            "LB": Motor(*drive_motors.LB),
            "RF": Motor(*drive_motors.RF),
            "RB": Motor(*drive_motors.RB)
        }

        self._motor = wpilib.Spark(robotmap.singlemotor.motorID)

    def set_power(self, Lpower=0, Rpower=None):
        if Rpower is None:
            # by default drive forward
            Rpower = Lpower
        
        self.motors["LF"].set(Lpower)
        self.motors["LB"].set(Lpower)

        self.motors["RF"].set(Rpower)
        self.motors["RB"].set(Rpower)


    def initDefaultCommand(self):
        self.setDefaultCommand(TankDriveJoystick())
