import wpilib

class SolenoidHandler():

    def __init__(self, port1, port2, _toget, _invert):
        self.sol1 = wpilib.Solenoid(port1)
        self.sol2 = wpilib.Solenoid(port2)
        self.toget = _toget
        self.invert = _invert
        self.deff = not _invert
        self.last = False
        self.sets(not self.deff)
    
    #No nessecary logic for the enable() and disable methods. WPIlib automatically does this.abs

    
    def enable(self):
        self.sol1.set(True)
        self.sol2.set(True)


    def disable(self):
        self.sol1.set(False)
        self.sol2.set(False)

    def get(self):
        return last
    
    def sets(self, on):
        if on is True:
            self.enable()
        else:
            self.disable()
            
    def toggle(self):
        sets(last)