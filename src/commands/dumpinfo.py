import time

from wpilib.command import Command

import subsystems

class DumpInfo(Command):
    """

    This dumps the info

    """

    def __init__(self):
        super().__init__('DumpInfo')
    
    def initialize(self):
        subsystems.tankdrive.encoders["L"].reset()
        subsystems.tankdrive.encoders["R"].reset()

    def execute(self):
        subsystems.dump_info()
