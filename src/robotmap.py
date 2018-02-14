"""

interface for the wires

Edit 1-20-2018: Encoder class created

"""

from enum import Enum


# roboRIO IP address
roborio = "roborio-3966-frc.local"


class InfoPasser:
    """
    
    Dummy class used to store variables on an object.
    
    """
    pass


class NavXType(Enum):

    I2C = 1
    SPI = 2


class Gearing(Enum):
    """

    Enum gearing

    """

    LOW = 0
    HIGH = 1




drive_motors = InfoPasser()

# L = left, R = right, F = front, B = back
# each object has (port, reverse)
drive_motors.LF = 0, False
drive_motors.LB = 1, False
drive_motors.RF = 2, True
drive_motors.RB = 3, True


extra_motors = InfoPasser()

extra_motors.arm_rotator_left = 4, False
extra_motors.arm_rotator_right = 5, False



drive_encoders = InfoPasser()

# Each encoder has two ports on the RoboRIO DIO
# Then, "inverted"
drive_encoders.L = 0, 1, True
drive_encoders.R = 2, 3, False

# range is a min, max of what speed (in ticks/time) are the encoders reading
# lowgear is for low gear readings and highgear is for high gear readings
# L.H = left high gear
# L.L = left low gear
drive_encoders.L_H = (-4.184, 4.768)
drive_encoders.L_L = (-2.213, 2.145)
drive_encoders.R_H = (-4.580, 4.870)
drive_encoders.R_L = (-2.197, 2.277)

# PID controller
pid_controllers = InfoPasser()

pid_controllers.drive = 0.12, 0.01, 0.0



axes = InfoPasser()

axes.L_x = 0
axes.L_y = 1

axes.R_x = 2
axes.R_y = 5


# triggers
axes.L_t = 3
axes.R_t = 4



solenoids = InfoPasser()

# solenoid ports
# main and complimentary ports and inverted
# port 0, port 1, isInverted
solenoids.gearshift = [(0, False), (1, True)]
solenoids.grabber = [(4, True), (5, False)]

# arm extender
solenoids.armextender = [(2, False), (3, True)]

#solenoids.gearshift1 


navx_type = NavXType.SPI

# PID Constant values for the encoders. CHECK OVER!!!!!
pid = InfoPasser()
pid.L = (0.18, 0, 0, 0)
pid.R = (0.18, 0, 0, 0)