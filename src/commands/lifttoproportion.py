from wpilib.command import Command
from wpilib.pidcontroller import PIDController

import subsystems
import oi

from robotmap import axes, pid, measures
from puremath.scaling import transform
import wpilib

'''
    Takes in the distance and applies it to the potentiometer. 
    Used for autonomous to allow for easy programming.
    PARAMS: 
    _dist - The distance that we want to extend the arm (~1-13 in)
    TODO: Create a puremath function that converts the pot reading to arm length
          Get Min and Max of arm w/ Pot reading
'''


class LiftToProportion(Command):
    def __init__(self, _setpoint):
        super().__init__("LiftToProportion")
        self.setpoint = _setpoint
        # setpoint is (from 0 to 1) a setpoint to set it to
        # TODO: Substitute in the min and max value in the transform() function

        self.PID = PIDController(12.0, 0.0, 0.0, subsystems.arm.get_arm_proportion, subsystems.arm.set_rotator)

        # TODO: Refine InputRange and AbsoluteTolerance
        self.PID.setInputRange(*measures.ROBOT_ARM_RANGE)
        self.PID.setAbsoluteTolerance(.005)

        self.PID.setContinuous(False)
        self.PID.setOutputRange(-1, 1)


    def initalize(self):
        self.PID.setSetpoint(self.setpoint)
        self.PID.enable()

    def isFinished(self):
        #return False
        return self.PID.onTarget()

    def execute(self):
        self.PID.setSetpoint(self.setpoint)
        self.PID.enable()

        #self.PID.enable()
        #print ("  !!!  EXEC")
        # Does this work? It feeds in a distance, 
        # and trys to get as close to that distance by manipulating the input and output.
        #self.PID.setSetpoint(self.setpoint)
        #pass
        #wpilib.SmartDashboard.putData("Pot PID", self.PID)

    def interrupted(self):
        self.end()
        #print (" !!! interrupted")

    def end(self):
        self.PID.disable()
        subsystems.arm.stop_rotator()
        #print (" !!! ended")
    