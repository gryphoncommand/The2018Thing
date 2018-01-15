
import wpilib
from wpilib import Spark

class Motor:
    """

    wrapper around the Spark motor

    """

    def __init__(self, index, inverted=False):
        self._motor = Spark(index)
        self.inverted = inverted


    def set(self, power=0.0):
        if self.inverted:
            power *= -1.0
        self._motor.set(power)


