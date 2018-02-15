import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes

class TankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('TankDriveJoystick')

        self.requires(subsystems.tankdrive)
        self.l_max = 0
        self.r_max = 0
        self.l_min = 0
        self.r_min = 0

    def initialize(self):
        pass

    def execute(self):
        lpow = oi.joystick.getRawAxis(axes.L_y)
        rpow = oi.joystick.getRawAxis(axes.R_y)

        subsystems.tankdrive.set(lpow, rpow)
        # if self.l_max < subsystems.tankdrive.encoders["L"].getRate():
        #     self.l_max = subsystems.tankdrive.encoders["L"].getRate()
        # if self.r_max < subsystems.tankdrive.encoders["R"].getRate():
        #     self.r_max = subsystems.tankdrive.encoders["R"].getRate()
        # if self.l_min > subsystems.tankdrive.encoders["L"].getRate():
        #     self.l_min = subsystems.tankdrive.encoders["L"].getRate()
        # if self.r_min > subsystems.tankdrive.encoders["R"].getRate():
        #     self.r_min = subsystems.tankdrive.encoders["R"].getRate()
        # smartdashboard.putNumber("L Enc Max", self.l_max)
        # smartdashboard.putNumber("L Enc Min", self.l_min)
        # smartdashboard.putNumber("R Enc Max", self.r_max)
        # smartdashboard.putNumber("R Enc Min", self.r_min)



        subsystems.smartdashboard.putString("tankdrive", str((lpow, rpow)))

    def end(self):
        subsystems.tankdrive.set(0, 0)
