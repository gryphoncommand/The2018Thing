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


class LiftToAngle(Command):
    def __init__(self, _angle):
        super().__init__("LiftToAngle")
        self.angle = _angle
        #to do need to also control second rotator motor

        # angle, in degrees, to rotate it:
        """

        'A' is about 45 degrees

        'B' is 0 degrees

        'C' is about -45 degrees

        |      A
        |    x
        |  x
        |x
        |----------B
        | x
        |   x
        |     x
        |       C

        """

        # TODO: Substitute in the min and max value in the transform() function
        def handle_pidout(x):
            print (x)
            print ("angle : " + str(subsystems.arm.get_arm_angle()))
            subsystems.arm.set_rotator(x)
        self.PID = PIDController(0.4, 0.0, 0.0, subsystems.arm.get_arm_angle, handle_pidout)

        # TODO: Refine InputRange and AbsoluteTolerance
        self.PID.setInputRange(*measures.ROBOT_ARM_ANGLE_RANGE)
        self.PID.setAbsoluteTolerance(1.0)

        self.PID.setContinuous(False)
        self.PID.setOutputRange(-1, 1)


    def initalize(self):
        self.PID.setSetpoint(self.angle)
        self.PID.enable()

    def isFinished(self):
        return self.PID.onTarget()

    def execute(self):
        self.PID.setSetpoint(self.angle)
        self.PID.enable()
        #self.PID.enable()
        #print ("  !!!  EXEC")
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
    