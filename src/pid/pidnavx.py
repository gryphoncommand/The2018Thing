from robotpy_ext.common_drivers import navx
from wpilib.interfaces.pidsource import PIDSource


class PIDNavXSource(PIDSource):
    def __init__(self, _navx):
        # Default values from ToastRhino, double and triple check.
        self.navx = _navx

        # Default PIDSourceType will be displacement until proven otherwise.
        self.setPIDSourceType(self.PIDSourceType.kDisplacement)

    def pidGet(self):
        # Simple checking of the Yaw (or z-axis)
        return self.navx.getYaw()
