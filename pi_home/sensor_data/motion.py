# use this to detect motion in the room, make a note of when the last detected motion was
# locally on the node rather than the server to negate the need for the server to save the
# node data locally, using persitant data store, i.e. a log file with the time saved
from datetime import datetime
import RPi.GPIO as GPIO

class motion():
    '''
        this class will store
            the last motion detection time
            a function to check the live data
    '''
    def __init__(self, pin = 23):
        '''
            this function initalises the class
            pin: int: this is what pin the motion sensor is set to using the BCM standard

        '''
        self.pin: int = pin
        self.last_movement: datetime = datetime(1970, 1, 1)
        self.movment_history: list[datetime] = []

    def get_live_data(self):
        try:
            # setting up the motion sensor
            m_pin: int = self.pin
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(m_pin, GPIO.IN)

            if GPIO.input(m_pin) == 1:
                now = datetime.now()
                self.movement_history.append(now)
                self.last_movement = now
                return (True, now)
            else:
                return False
        except Exception as e:
            return ("unknown error occured", e)

    def get_history(self, length: str = 'l'):
        """
            this function will search through the .sensor_data folder for the last recorded movement
            length: str if 'l' will return last movement, if 'a' will return all history
        """

        if length.lower() == 'l':
            return self.last_movement
        elif length.lower() == 'a':
            return self.movement_history
        else:
            raise ValueError(
                    f"""
                    length must be 'l', lima, or 'a', alpha, case insensitive.
                    Actual value{length}
                    """
                )


