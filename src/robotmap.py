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


drive_encoders = InfoPasser()

# Each encoder has two ports on the RoboRIO DIO
# Then, "inverted"
drive_encoders.L = 0, 1, True
drive_encoders.R = 2, 3, False

# distance per pulse
drive_encoders.L_dpp = 1.0/1610.0
drive_encoders.R_dpp = 1.0/1610.0

# range is a min, max of what speed (in ticks/time) are the encoders reading
# lowgear is for low gear readings and highgear is for high gear readings
# Left Encoder - 2454 Ticks in ~5 Feet
# Right Encoder - 2414 Ticks in ~5 Feet
# L.H = left high gear
# L.L = left low gear
drive_encoders.L_H = (-4.184, 4.768)
drive_encoders.L_L = (-2.213, 2.145)
drive_encoders.R_H = (-4.580, 4.870)
drive_encoders.R_L = (-2.197, 2.277)


# was extra_motors
arm_motors = InfoPasser()
arm_motors.L = 4, False
arm_motors.R = 5, False

arm_encoders = InfoPasser()

# Each encoder has two ports on the RoboRIO DIO
# Then, "inverted"
arm_encoders.L = 4, 5, True
arm_encoders.R = 6, 7, False



# PID controller


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
pid.L = (0.24, .02, 0, 0)
pid.R = (0.24, .02, 0, 0)
pid.dist_L = (2, 0, 0, 0)
pid.dist_R = (2, 0, 0, 0)
pid.angle = (0.03, 0, 0, 0)

