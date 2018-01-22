"""

interface for the wires

Edit 1-20-2018: Encoder class created

"""

from enum import Enum


roborio = "roborio-3966-frc.local"


class InfoPasser:
    """
    
    Dummy class used to store variables on an object.
    
    """
    pass


class NavXType(Enum):

    I2C = 1
    SPI = 2



drive_motors = InfoPasser()

# L = left, R = right, F = front, B = back
# each object has (port, reverse)
drive_motors.LF = 0, False
drive_motors.LB = 1, False
drive_motors.RF = 2, True
drive_motors.RB = 3, True


encoders = InfoPasser()

#E = Encoder
#Each encoder has two ports on the RoboRIO DIO

encoders.LF = 0
encoders.LB = 1
encoders.RF = 2
encoders.RB = 3



axes = InfoPasser()

axes.L_x = 0
axes.L_y = 1

axes.R_x = 2
axes.R_y = 5



solenoids = InfoPasser()

# solenoid ports
# main and complimentary ports and inverted
# port 0, port 1, isInverted
solenoids.gearshift = (2, 3, False)

#solenoids.gearshift1 


navx_type = NavXType.SPI


