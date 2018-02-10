from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi

from robotmap import axes, pid
import wpilib

'''
    Takes in the distance and applies it to the potentiometer. 
    Used for autonomous to allow for easy programming.
    PARAMS: 
    _dist - The distance that we want to extend the arm (~1-13 in)
    TODO: Create a puremath function that converts the pot reading to arm length
          Get Min and Max of arm w/ Pot reading
'''

class LiftToAngle(Command):
    def __init__(self, _dist):
        self.dist = _dist
        self.out = PIDMotorOutput(subsystems.arm.rotator_motor)

        # Probably replace the pot.pidGet() with a function, from puremath, 
        # that converts the pidGet() into a distance.
        self.PID = PIDController(0.03, 0.0, 0.0, subsystems.tankdrive.pot.pidGet, subsystems.arm.set_rotator

        # TODO: Refine InputRange and AbsoluteTolerance
        self.PID.setInputRange(0, 10)
        self.PID.setAbsoluteTolerance(10)

        self.PID.setContinuous(True)
        self.PID.setOutputRange(-1, 1)


    def initalize(self):
        self.PID.enable()

    def isFinished(self):
        return self.PID.onTarget()

    def execute(self):
        # Does this work? It feeds in a distance, 
        # and trys to get as close to that distance by manipulating the input and output.
        self.PID.setSetpoint(self.dist)
        wpilib.SmartDashboard.putData("Pot PID", self.PID)

    def interrupted(self):
        self.end()

    def end(self):
        self.PID.disable()
        subsystems.arm.stop_rotator()
    