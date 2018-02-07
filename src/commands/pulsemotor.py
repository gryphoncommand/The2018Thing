from wpilib.command import Command

import subsystems
import oi
import math
import time


from robotmap import axes


class PulseMotor(Command):
    """

    Joystick control the tank drive

    """

    def __init__(self):
        super().__init__('PulseMotor')

        self.requires(subsystems.tankdrive)

        self.stime = None

    def execute(self):
        ctime = time.time()

        if self.stime is None:
            self.stime = ctime

        dtime = ctime - self.stime

        lpow = math.sin(dtime * 2)
        rpow = math.cos(dtime * 3)
        subsystems.tankdrive.set_power(lpow, rpow)

    def end(self):
        subsystems.tankdrive.set_power(0, 0)

        self.stime = None
