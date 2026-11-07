from gpiozero import DistanceSensor as DS

class sonics():
    '''
        this class will be used to gain information from the ultra sonic sensor
    '''
    def __init__(self, echo: int = 12, trigger: int = 16):
        '''
            echo: int, GPIO pin number (NOT BCM)
            trigger: int, GPIO pin number (NOT BCM)
        '''
        self._se = DS(echo=echo, trigger=trigger)

    def distance(self):
        return self._se.distance * 100
