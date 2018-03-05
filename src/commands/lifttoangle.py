from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi

from robotmap import axes, pid, measures
from puremath import transform
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
    def __init__(self, _angle):
        self.angle = _angle
        #to do need to also control second rotator motor

        # TODO: Substitute in the min and max value in the transform() function
        self.PID = PIDController(0.03, 0.0, 0.0, subsystems.arm.get_arm_proportion, subsystems.arm.set_rotator)

        # TODO: Refine InputRange and AbsoluteTolerance
        self.PID.setInputRange(0, 1)
        self.PID.setAbsoluteTolerance(0.03)

        self.PID.setContinuous(False)
        self.PID.setOutputRange(-1, 1)


    def initalize(self):
        self.setpoint = transform(self.angle, measures.ROBOT_ARM_ANGLE_RANGE, (0, 1))

        self.PID.setSetpoint(self.setpoint)
        self.PID.enable()

    def isFinished(self):
        return self.PID.onTarget()

    def execute(self):
        # Does this work? It feeds in a distance, 
        # and trys to get as close to that distance by manipulating the input and output.
        #self.PID.setSetpoint(self.setpoint)
        pass
        #wpilib.SmartDashboard.putData("Pot PID", self.PID)

    def interrupted(self):
        self.end()

    def end(self):
        self.PID.disable()
        subsystems.arm.stop_rotator()
    