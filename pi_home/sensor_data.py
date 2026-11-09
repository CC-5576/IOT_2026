import RPi.GPIO as GPIO
from   lib import dht, board
from   datetime import datetime
from   time import time
from   gpiozero import DistanceSensor


class Window:
    def __init__(self, pin: int = 19):
        GPIO.setup(pin, GPIO.IN)
        self.pin = pin

    def status(self):
        if GPIO.input(self.pin) == 1:
            return "open"
        else:
            return "closed"


class HumidTemp:
    """
    This class will store the last reading of the temperature and humidity sensor
    """

    def __init__(self):
        self._sensor_ = dht.DHT11(board.D4)
        self._last_readings_: (float, int) = (0, 0)

    def update(self) -> (float, int):
        "this function will update the sensor reading and return a tuple containing the temperature and humidity"
        self._last_readings_ = (self._sensor_.temperature, self._sensor_.humidity)
        return self._last_readings_

    def read(self):
        if self._last_readings_ == (0, 0):
            self.update()
        return self._last_readings_


class Motion:
    """
    this class will store
        the last motion detection time
        a function to check the live data
    """

    def __init__(self, pin=23):
        """
        this function initalises the class
        pin: int: this is what pin the motion sensor is set to using the BCM standard

        """
        self.pin: int = pin
        self.default = "1970-01-01T00:00:00"
        self._movement_history: list[str] = [self.default]

    def get_live_data(self):
        # setting up the motion sensor
        m_pin: int = self.pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(m_pin, GPIO.IN)
        
        et = time()+30
        movement = False
        while time() < et:
            if GPIO.input(m_pin) == 1:
                now: datetime = datetime.now().isoformat()
                self._movement_history.append(now)
                movement = True
                break

        if movement:
            return True, self._movement_history[-1]
        else:
            return False
                

    def get_history(self, length: str = "l"):
        """
        this function will search through the .sensor_data folder for the last recorded movement
        length: str if 'l' will return last movement, if 'a' will return all history
        """

        if length.lower() == "l":
            # if last movment is the defalt (1970,1,1), then check movment
            if self._movement_history[-1] == self.default:
                self.get_live_data()

            return self._movement_history[-1]

        elif length.lower() == "a":
            # if there is no movment history, then get live data
            if self._movement_history == []:
                self.get_live_data()

            return self._movement_history
        else:
            raise ValueError(
                f"""
                    length must be 'L' or 'A', case insensitive.
                    Actual value: {length}
                    """
            )


class Sonics:
    """
    this class will be used to gain information from the ultra sonic sensor
    """

    def __init__(self, echo: int = 12, trigger: int = 16):
        """
        echo: int, GPIO pin number (NOT BCM)
        trigger: int, GPIO pin number (NOT BCM)
        """
        self._se = DistanceSensor(echo=echo, trigger=trigger)

    def distance(self):
        return self._se.distance * 100


class Sound:
    """
    this will be used to return if there is noise from the microphone
    default microphone pin is 24, change with pin=00
    default microphone sensitivity is set to an average of 0.05 over a 30 second window.
        to adjust you can either adjust the microphone it's self, or the average in software.
        this average is changeable by calling this function with avg=0.00
    """

    def __init__(self, pin=24, avg=0.05):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pin = pin
        self.avg = 0.05

    def detect(self):
        et = time() + 30
        noise_detection = []
        while time() < et:
            noise_detection.append(GPIO.input(self.pin))
        avg = sum(noise_detection) / len(noise_detection)
        print(avg, len(noise_detection))
        if avg <= self.avg:
            return "no noise detected"
        elif avg > self.avg:
            return "noise detected"
        # based on a testing, an average greater than 0.1

__all__=['Window', 'HumidTemp', 'Motion', 'Sonics', 'Sound']
