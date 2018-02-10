import time

from wpilib.command import Command

import subsystems
import oi
import wpilib
from robotmap import axes


class TankDriveJoystick(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('TankDriveJoystick')

        self.requires(subsystems.tankdrive)

    def initialize(self):
        self.Lmax = 0
        self.Rmax = 0


    def execute(self):
        joy = oi.get_joystick()
        lpow = joy.getRawAxis(axes.L_y)
        rpow = joy.getRawAxis(axes.R_y)

        subsystems.tankdrive.set(lpow, rpow)

        self.reading = subsystems.tankdrive.encoders["L"].getRate()
        self.Rreading = subsystems.tankdrive.encoders["R"].getRate()
        if self.Lmax > self.reading:
            self.Lmax = self.reading
        if self.Rmax > self.Rreading:
            self.Rmax = self.Rreading


        subsystems.smartdashboard.putString("tankdrive", str((lpow, rpow)))
        # subsystems.smartdashboard.putNumber("Ticks", subsystems.tankdrive.encoders["L"].get())
        wpilib.SmartDashboard.putNumber("Left Encoder", self.Lmax)
        wpilib.SmartDashboard.putNumber("Right Encoder", self.Rmax)

    def end(self):
        subsystems.tankdrive.set(0, 0)
