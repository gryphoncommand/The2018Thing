import time

from wpilib.command import Command

import subsystems
import oi

from robotmap import axes

import recordplayback
from recordplayback import ControllerSamples


class Record(Command):
    """

    Record joystick info while running a command

    """

    def __init__(self, filename="test_macro.csv", concurrent_command=None, record_timeout=8.0, record_interval=.02, record_axes=[0, 1, 2, 3, 4, 5], record_buttons=[1, 2, 3, 4, 5]):
        name = "Record"
        if concurrent_command is not None:
            name += "[%s]" % type(concurrent_command).__name__
        super().__init__(name)

        self.filename = filename
        self.concurrent_command = concurrent_command
        
        self.record_timeout = record_timeout
        self.record_interval = record_interval

        self.record_axes = record_axes
        self.record_buttons = record_buttons

        if self.record_timeout is not None:
            self.setTimeout(self.record_timeout)

        self.sampler = ControllerSamples()


    def initialize(self):
        self.samples = ControllerSamples()

        if self.concurrent_command is not None:
            self.concurrent_command.initialize()

    def execute(self):
        joy = oi.get_joystick()

        sample_dict = {
            "axes": {
            },
            "buttons": {
            }
        }

        for axis in self.record_axes:
            sample_dict["axes"][axis] = joy.getRawAxis(axis)

        for button in self.record_buttons:
            sample_dict["buttons"][button] = joy.getRawButton(button)

        self.samples.add_reading(sample_dict)

        if self.concurrent_command is not None:
            self.concurrent_command.execute()

    def isFinished(self):
        if self.concurrent_command is not None:
            return self.isTimedOut() or self.concurrent_command.isTimedOut()
        else:
            return self.isTimedOut()

    def end(self):
        if self.concurrent_command is not None:
            self.concurrent_command.end()

        self.samples.force_interval(self.record_interval)

        full_filename = recordplayback.macro_dir + self.filename

        print ("saving to " + full_filename)

        fp = open(full_filename, "w")

        fp.write(str(self.samples))

        fp.close()

    def interrupted(self):
        self.end()
