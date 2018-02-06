from wpilib.analogpotentiometer import AnalogPotentiometer
from wpilib.interfaces.pidsource import PIDSource
from wpilib.interfaces.pidoutput import PIDOutput


class PIDPotSource(PIDSource):
    def __init__(self):
        # Default values from ToastRhino, double and triple check. 
        self.pot = AnalogPotentiometer(2, 100, -20)

        # Default PIDSourceType will be distance until proven otherwise. 
        self.setPIDSourceType(PIDSource.PIDSourceType.kDisplacement)

    def pidGet(self):
        # Simple checking of SourceType
        if self.getPIDSourceType() == PIDSource.PIDSourceType.kDisplacement:
            return self.pot.get()
        else:
            print("Dude, how did you mess this up? [Pot PIDSourceError]")
