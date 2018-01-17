"""

Module for recording and playing back auto/macro programs

"""

import os
import time

macro_dir = None

ROBORIO_DEFAULT_MACRODIR = "/home/lvuser/macro_dir"
NORMAL_DEFAULT_MACRODIR = os.getcwd() + "/local_macro_dir"

if os.path.isdir("/home/lvuser"):
    # we are on the roboRIO
    macro_dir = ROBORIO_DEFAULT_MACRODIR
else:
    # we are on a laptop simulating the code
    macro_dir = NORMAL_DEFAULT_MACRODIR


if macro_dir is not None:
    if not os.path.isdir(macro_dir):
        os.makedirs(macro_dir)
    macro_dir += "/"


class ControllerSamples:
    """

    Class to store and receive controller samples

    Example sample looks like:
    time, {
        "axes": {
            0: .65,
            2: .32,
            ...
        },
        "buttons": {
            0: True,
            3: False,
            ...
        }
    }

    """
    def __init__(self, strval=None):
        self.readings = []
        self.started_reading = None
        if strval is not None:
            # parse the string
            self.unserialize(strval)

    def clear(self):
        """

        clear all readings

        """

        self.readings = []
        self.started_reading = None

    def serialize_reading(self, reading):
        """

        Serialization format is like this:

        (time is first)

        (buttons are 0==False and 1==True)

        0.0,AXES,0=VAL,1=VAL,3=VAL,BUTTONS,0=0,1=1

        """
        rel_time, samples = reading
        ret_str = ""
        ret_str += "%.4f,AXES" % rel_time
        for axis in samples["axes"]:
            ret_str += ",%d=%.4f" % (axis, samples["axes"][axis])
        ret_str += ",BUTTONS"
        convert_bool = lambda x: 1 if x else 0
        for button in samples["buttons"]:
            ret_str += ",%d=%d" % (button, convert_bool(samples["buttons"][button]))
        return ret_str

    def unserialize_reading(self, reading_str):
        t_part, rest = reading_str.split("AXES")
        t_part = t_part.replace(",", "")
        rel_time = float(t_part)
        axes_str, buttons_str = rest.split("BUTTONS")

        samples = {
            "axes": {},
            "buttons": {}
        }
        
        axes_str = list(filter(lambda x: len(x) > 0, axes_str.split(",")))
        for axis_str in axes_str:
            k, v = axis_str.split("=")
            k = int(k)
            v = float(v)
            samples["axes"][k] = v

        int_to_bool = lambda x: True if x == 1 else False
        buttons_str = list(filter(lambda x: len(x) > 0, buttons_str.split(",")))
        for button_str in buttons_str:
            k, v = button_str.split("=")
            k = int(k)
            v = int_to_bool(int(v)) #
            samples["buttons"][k] = v
        
        return rel_time, samples

    def serialize(self):
        """

        returns complete string representation of object, with newlines breaking readings

        """
        ret_str = ""
        for r in self.readings:
            ret_str += self.serialize_reading(r) + "\n"
        return ret_str

    def unserialize(self, str_val):
        """

        Sets the current readings to the unserialized readings

        """

        samples_str = list(filter(lambda x: len(x) > 0, str_val.split("\n")))
        for sample_str in samples_str:
            cur_reading = self.unserialize_reading(sample_str)
            self.readings += [cur_reading]

        # sort by time
        self.readings = sorted(self.readings, key=lambda x: x[0])

    
    __str__ = serialize

    def start_reading(self):
        self.started_reading = time.time()

    def add_reading(self, reading, rel_time=None):
        if rel_time is None and self.started_reading is None:
            self.start_reading()
        
        if rel_time is None:
            rel_time = time.time() - self.started_reading

        sample_tuple = (rel_time, reading)
        self.readings += [sample_tuple]

    def force_interval(self, interval=.02):
        """

        record at maximum once every interval, deleting extras

        """

        result_readings = []

        cur_interval = 0.0

        i = 0

        while i < len(self.readings):
            result_readings += [self.readings[i]]
            i += 1
            while i < len(self.readings) and self.readings[i][0] < cur_interval + interval:
                i += 1
            cur_interval += interval

        self.readings = result_readings


    def __len__(self):
        return len(self.readings)
    
    def __getitem__(self, key):
        return self.readings[key]



class MockController:
    """

    Class to playback acting as a controller, giving it a ControllerSamples object

    """
    
    def __init__(self, _samples):
        self._samples = _samples
    
        self.stime = None

        self.current_reading = None
        self.reading_idx = 0

        self.max_time = max([i[0] for i in self._samples])


    def reset_timer(self):
        self.stime = None
        self.reading_idx = 0
        
    
    def start_reading(self):
        self.stime = time.time()
        self.reading_idx = 0
    
    def isTimedOut(self):
        if self.stime is None:
            return True
        else:
            return (time.time() - self.stime) > self.max_time

    def __update(self):
        if self.stime is None:
            self.start_reading()

        ctime = time.time() - self.stime

        while self.reading_idx < len(self._samples):
            rel_time, samples = self._samples[self.reading_idx]
            if rel_time <= ctime:
                self.current_reading = rel_time, samples
                self.reading_idx += 1
            else:
                break


    def getRawAxis(self, axis):
        self.__update()
        #next_reading = self._samples[self.reading_idx + 1]
        return self.current_reading[1]["axes"][axis]

