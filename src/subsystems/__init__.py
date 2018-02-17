"""

All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.

"""

from wpilib.robotbase import RobotBase

from networktables import NetworkTables
from wpilib.driverstation import DriverStation
import wpilib

from .tankdrive import TankDrive
from .sensors import Sensors
from .arm import Arm


import robotmap

tankdrive = None
sensors = None
arm = None

smartdashboard = None
infotable = None

is_init = False


def init():
    """

    instansiates all subsystems. Needs to be a method so it isn't ran on import

    """
    global tankdrive; global sensors; global arm; global smartdashboard; global infotable; global is_init

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
    arm = Arm()

    smartdashboard = NetworkTables.getTable('SmartDashboard')
    infotable = NetworkTables.getTable('info')


def dump_info():
    if hasattr(tankdrive, "encoders"):
        smartdashboard.putNumber("L Encoder Speed", tankdrive.encoders["L"].getRate())
        smartdashboard.putNumber("R Encoder Speed", tankdrive.encoders["R"].getRate())

        smartdashboard.putNumber("L Encoder Distance", tankdrive.encoders["L"].getDistance())
        smartdashboard.putNumber("R Encoder Distance", tankdrive.encoders["R"].getDistance())


    smartdashboard.putNumber("Battery Voltage", DriverStation.getInstance().getBatteryVoltage())
    smartdashboard.putString("NavX Displacement (X, Y, Z)", str(sensors.navx.getDisplacement()))
    smartdashboard.putNumber("NavX Yaw", sensors.navx.getYaw())
    

