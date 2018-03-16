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
        smartdashboard.putNumber("left_enc_speed", tankdrive.encoders["L"].getRate())
        smartdashboard.putNumber("left_enc_distance", tankdrive.encoders["L"].getDistance())

        smartdashboard.putNumber("right_enc_speed", tankdrive.encoders["R"].getRate())
        smartdashboard.putNumber("right_enc_distance", tankdrive.encoders["R"].getDistance())

    smartdashboard.putNumber("arm_proportion", arm.get_arm_proportion())
    smartdashboard.putNumber("battery_voltage", DriverStation.getInstance().getBatteryVoltage())

    disp = sensors.navx.getDisplacement()

    smartdashboard.putNumber("navx_distance_x", disp[0])
    smartdashboard.putNumber("navx_distance_y", disp[1])
    smartdashboard.putNumber("navx_distance_z", disp[2])

    smartdashboard.putNumber("navx_yaw", sensors.navx.getYaw())

    smartdashboard.putNumber("pressure_psi", sensors.get_pressure())


    game_data = None

    try:
        game_data = DriverStation.getInstance().getGameSpecificMessage()
    except Exception as e:
        print (" !!! EXCEPTION:  " + str(e))

    smartdashboard.putString("game_data", str(game_data))

    # DEBUG

    smartdashboard.putNumber("[TMP] arm ticks", arm.rotator_encoders["R"].get())



    wpilib.LiveWindow.run()


"""
Following the Equation given to us in the Analog Pressure Sensor Datasheet:

    p = 250(Out/Supply) - 25
    
    p - pressure
    Out - Output Voltage
    Supply - Supply Voltage (Usually 5 Volts) [In robotmap]
"""
