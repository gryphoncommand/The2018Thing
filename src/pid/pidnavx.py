from wpilib.analogpotentiometer import AnalogPotentiometer
from wpilib.interfaces.pidsource import PIDSource


class PIDNavXSource(PIDSource):
    def __init__(self, _navx):
        self.navx = _navx

        # Default PIDSourceType will be displacement.  

    def pidGet(self):
        # Simple checking of SourceType
        v = self.navx.getYaw()
        return v

    def setPIDSourceType(self, v):
        if v != PIDSource.PIDSourceType.kDisplacement:
            raise Exception("Must use displacement for navx")

    def getPIDSourceType(self):
        return PIDSource.PIDSourceType.kDisplacement
