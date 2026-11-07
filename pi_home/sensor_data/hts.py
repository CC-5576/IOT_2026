import board
import adafruit_dht as dht

class HumidTemp():
    '''
        This class will store the last reading of the temperature and humidity sensor
    '''
    def __init__(self):
        self._sensor_ = dht.DHT11(board.D4)
        self._last_readings_: (float, int) = (0,0)

    def update(self) -> (float, int):
        'this function will update the sensor reading and return a tuple containing the temperature and humidity'
        self._last_readings_ = (self._sensor_.temperature, self._sensor_.humidity)
        return self._last_readings_

    def read(self):
        return self._last_readings_

