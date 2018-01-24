"""

these are scaling functions, used for joysticks

These return lambdas/local functions

"""


def no_scaling(tweak=0.0):
    # tweak doesn't do anything, just there for others
    def my_scaler(x):
        return x
    return my_scaler

def poly_scaling(tweak=1.0):
    # simple polynomial scaling, see this desmos:
    # https://www.desmos.com/calculator/eu8pt43bqf
    thresh = 0.025
    if tweak <= thresh
        tweak = thresh
    
    def my_scaler(x):
        abs_x = abs(x)
        sign = 1.0 if x > 0.0 else -1.0
        if abs_x == 0.0:
            return 0.0
        else:
            return sign * (abs_x ** float(tweak))
    return my_scaler

