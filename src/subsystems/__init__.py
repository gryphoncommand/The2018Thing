"""

All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.

"""

from wpilib.robotbase import RobotBase

from .tankdrive import TankDrive
from .subsystems import Subsystems

tankdrive = None

def init():
    """

    instansiates all subsystems. Needs to be a method so it isn't ran on import

    """
    global tankdrive

    """

    Some tests call startCompetition multiple times, so don't throw an error if
    called more than once in that case.

    """
    if tankdrive is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    tankdrive = TankDrive()
