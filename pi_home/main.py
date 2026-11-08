from pi_home.lib import S7
from pi_home.sensor_data import *
from pi_home.network_comms import Node

import asyncio
import json
from datetime import datetime

default_port = 16576


class sensors:
    def __init__(self):
        '''this will setup and store the instants sensor suit'''
        self._Window = Window()
        self._Temperature = HumidTemp()
        self._Motion = motion()
        self._Sonics = sonics()
        self._Sound = sound()
        self.window: None|str = None
        self.temperature: None|float = None
        self.humidity: None|int = None
        self.motion: None|datetime = None
        self.door_distance: None|float = None
        self.sound_detection: None|str = None

    def update(self):
        # check if the window is open
        self.window = self._Window.status()

        # check the temperature and humidity
        self.temperture, self.humidity = self._Temperature.update()

        # check for movment and return last movement
        self._Motion.get_live_data()
        self.motion = self._Motion.get_history()

        # check if the door is open
        self.door_distance = self._Sonics.distance()

        # sound detecion
        self.soud_detection = self._Sound.detect()


    def dataFormatter(self):
        return json.dumps({
            "Wind": self.window,
            "Temp": self.temperature,
            "Humi": self.humidity,
            "Moti": self.motion,
            "Soni": self.door_distance,
            "Soun": self.sound_detection,
        })


async def main():
    asyncio.run(node(None, default_port))
    

    
