import wpilib

'''
A class that creates solenoids.
Used to create gearshifting in the oi.py 

Created on 1-20-2018 by Tyler Duckworth
'''

class SolenoidHandler():

    def __init__(self, port0, port1, inverted=False):
        self.port0, self.port1 = port0, port1
        self.inverted = inverted
        self.sol0 = wpilib.Solenoid(port0)
        self.sol1 = wpilib.Solenoid(port1)

        self.last = False
    
    def enable(self):
        self.last = True
        self.sol0.set(True)
        self.sol1.set(True)

    def disable(self):
        self.last = False
        self.sol0.set(False)
        self.sol1.set(False)

    def get(self):
        return last
    
    def set(self, on):
        if on:
            self.enable()
        else:
            self.disable()
            
    def toggle(self):
        self.set(not self.last)
