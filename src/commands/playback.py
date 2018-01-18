import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes

import recordplayback
from recordplayback import ControllerSamples


class Playback(Command):
    """

    Plays back a macro with another command

    """

    def __init__(self, filename="test_macro.csv", concurrent_command=None, timeout=None):
        name = "Playback[%s]" % filename
        if concurrent_command is not None:
            name += "[%s]" % type(concurrent_command).__name__

        super().__init__(name)

        self.timeout = timeout

        self.filename = filename
        self.concurrent_command = concurrent_command
        
        if self.timeout is not None:
            self.setTimeout(self.timeout)


    def initialize(self):
        self.samples = ControllerSamples()

        oi.set_default_joystick_key(self.filename)
        oi.get_joystick(key=self.filename).reset_timer()

        if self.concurrent_command is not None:
            self.concurrent_command.initialize()

    def execute(self):
        if self.concurrent_command is not None:
            self.concurrent_command.execute()

    def isFinished(self):
        if oi.get_joystick(key=self.filename).isTimedOut():
            return True
        
        if self.concurrent_command is not None and self.concurrent_command.isFinished():
            return True
        
        if self.timeout != None and self.isTimedOut():
            return True

        return False

    def end(self):
        if self.concurrent_command is not None:
            self.concurrent_command.end()

        oi.set_default_joystick_key(0)

    def interrupted(self):
        self.end()
