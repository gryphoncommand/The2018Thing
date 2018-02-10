from wpilib.interfaces.pidsource import PIDSource


class PIDPotSource(PIDSource):
    def __init__(self, _pot):
        # Takes potentiometer as parameter to prevent possible HAL errors
        self.pot = _pot

        # Default PIDSourceType will be distance until proven otherwise. 
        self.setPIDSourceType(PIDSource.PIDSourceType.kDisplacement)

    def pidGet(self):
        # Simple checking of SourceType
        if self.getPIDSourceType() == PIDSource.PIDSourceType.kDisplacement:
            return self.pot.get()
        else:
            print("Dude, how did you mess this up? [Pot PIDSourceError]")
