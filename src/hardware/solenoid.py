import wpilib

'''
A class that creates solenoids.
Used to create gearshifting in the oi.py 

Created on 1-20-2018 by Tyler Duckworth
'''

class SolenoidHandler():

    def __init__(self, *ports):
        """

        Call like: SolenoidHandler((0, False), (1, True), ... (port, isInverted))

        """
        self.ports = ports
        self.sols = []
        for port, invert in self.ports:
            self.sols += [(wpilib.Solenoid(port), invert)]

        self.last = False

    def get(self):
        return self.last
    
    def enable(self):
        self.last = True
        for sol, invert in self.sols:
            sol.set(not invert)

    def disable(self):
        self.last = False
        for sol, invert in self.sols:
            sol.set(invert)

    def get(self):
        return self.last
    
    def set(self, on):
        if on:
            self.enable()
        else:
            self.disable()
            
    def toggle(self):
        self.set(not self.last)
