import wpilib
from wpilib.interfaces.pidsource import PIDSource
from networktables import NetworkTables
import subsystems


class PIDnt(PIDSource):
    def __init__(self, _var, _var1):
        self.center = _var
        self.radius = _var1

    def pidGet(self):
        self.val = subsystems.smartdashboard.getNumber(self.center)
        self.val1 = subsystems.smartdashboard.getNumber(self.radius)
        if self.val < -1:
            raise EnvironmentError("Invalid X-coordinate")
        if self.val1 < -1:
            raise EnvironmentError("Invalid radius")
        return self.val
