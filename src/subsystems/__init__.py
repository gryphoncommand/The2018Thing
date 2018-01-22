"""

All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.

"""

from wpilib.robotbase import RobotBase

from networktables import NetworkTables 
from wpilib.driverstation import DriverStation

from .tankdrive import TankDrive
from .sensors import Sensors


import robotmap

tankdrive = None
sensors = None

smartdashboard = None
infotable = None

is_init = False


def init():
    """

    instansiates all subsystems. Needs to be a method so it isn't ran on import

    """
    global tankdrive; global sensors; global smartdashboard; global infotable; global is_init

    """

    Some tests call startCompetition multiple times, so don't throw an error if
    called more than once in that case.

    """
    
    if is_init and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    if is_init:
        return

    is_init = True

    tankdrive = TankDrive()
    sensors = Sensors()

    smartdashboard = NetworkTables.getTable('SmartDashboard')
    infotable = NetworkTables.getTable('info')


def dump_info():
    smartdashboard.putNumber("Battery Voltage", DriverStation.getInstance().getBatteryVoltage())
    smartdashboard.putNumberArray("NavX Displacement [X, Y, Z]", sensors.navx.getDisplacement())
    

