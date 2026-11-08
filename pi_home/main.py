from .lib import S7
from .sensor_data import *
from .network_comms import Node

import asyncio
import json
from time import sleep, time

def dataFormatter(Wind, Temp, Humi, Moti, Soni, Soun):
    return json.dumps({
        "Wind": Wind,
        "Temp": Temp,
        "Humi": Humi,
        "Moti": Moti,
        "Soni": Soni,
        "Soun": Soun,
        })

class sensors:
    def __init__(self):
        '''this will setup and store the instants sensor suit'''
        self.Window = Window.

async def main():
    
    
