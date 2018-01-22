"""

NavX wrapper

"""

import robotmap

from robotpy_ext.common_drivers import navx

class NavX:

    def __init__(self, navx_type):
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

        


    

