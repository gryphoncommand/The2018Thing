from wpilib.analogpotentiometer import AnalogPotentiometer
from wpilib.interfaces.pidsource import PIDSource


class PIDNavXSource(PIDSource):
    def __init__(self, _navx):
        self.navx = _navx

        # Default PIDSourceType will be displacement.  
        self.setPIDSourceType(PIDSource.PIDSourceType.kDisplacement)

    def pidGet(self):
        # Simple checking of SourceType
        if self.getPIDSourceType() == PIDSource.PIDSourceType.kDisplacement:
            return self.navx.getYaw()
        else:
            raise TypeError("Invalid NavX PIDSourceType")
