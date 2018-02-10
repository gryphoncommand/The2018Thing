
from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi
from pid.pidpot import PIDPotSource
from pid.pidmotor import PIDMotorSource, PIDMotorOutput

from robotmap import axes, pid
import wpilib

'''
    Takes in the distance
'''

class LiftToAngle(Command):
    def __init__(self, _dist):
        self.dist = _dist
        self.source = PIDPotSource(subsystems.sensors.pot)
        self.out = PIDMotorOutput(subsystems.arm.rotator_motor)

        self.PID = PIDController(0.03, 0.0, 0.0, self.source, self.out)

        # TODO: Refine InputRange
        self.PID.setInputRange(0, 10)
        self.PID.setContinuous(True)
        self.PID.setOutputRange(-1, 1)

    # A function we will use to approximate the extension of the arm from the pot reading.
    # TODO: Move this (preferably functioning) to the Potentiometer File.
    def calcFunction(self, distance):
        return distance

    def initalize(self):
        self.reading = self.source.pidGet() + self.dist

    def isFinished(self):
        pass

    def execute(self):
        pass

    def interrupted(self):
        pass

    def end(self):
        pass
    