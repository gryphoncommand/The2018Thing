"""

NavX wrapper

"""

import robotmap

from robotpy_ext.common_drivers import navx

class NavX:

    def __init__(self, navx_type):
        self.prev_x_accel = 0
        self.prev_y_accel = 0
        if navx_type is robotmap.NavXType.I2C:
            self.navx = navx.AHRS.create_i2c()
        elif navx_type is robotmap.NavXType.SPI:
            self.navx = navx.AHRS.create_spi()
        else:
            print ("warning navx instaniated with unknown navx_type")


    def getDisplacement(self):
        """
        
        if the navx doesn't support displacement, it will return a rough estimation, and won't fail

        """
        return self.navx.getDisplacementX(), self.navx.getDisplacementY(), self.navx.getDisplacementZ()


    def getYaw(self):
        '''

        Gets the yaw, or z-axis for the robot. Helpful for angle calculations.

        '''
        return self.navx.getYaw()

    """
    This is ported code from https://www.pdocs.kauailabs.com/navx-mxp/examples/collision-detection/ to see if RobotPy could implement something like this. 

    Note: This should be a command instead of in here.

    def collision(self, threshold, isEnabled):
        '''

        Parameters:
            Threshold, in Gs, at which a hit is considered a collision.
            isEnabled - A boolean that will show if the robot is enabled.
        WARNING: NOT STABLE

        '''

        self.collisionDetected = False

        while isEnabled:

            self.current_x_accel = self.navx.getWorldLinearAccelX()
            self.current_Jerk_x = self.current_x_accel - self.prev_x_accel
            self.prev_x_accel = self.current_x_accel
            self.current_y_accel = self.navx.getWorldLinearAccelY()
            self.current_Jerk_y = self.current_y_accel - self.prev_y_accel
            self.prev_y_accel = self.current_y_accel

            if abs(self.current_Jerk_x) == threshold and abs(self.current_Jerk_y) == threshold:
                self.collisionDetected = True
        return self.collisionDetected
    """

    

