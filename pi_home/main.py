from lib import S7
from sensor_data import *
from output import *

import asyncio
import json
from datetime import datetime
import RPi.GPIO as GPIO


class NodeServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print(f'Data received: {message}')
        
        if message == "0x01":
            Live_Sensors.update()
            transmission_data = str(Live_Sensors.dataFormatter()).encode("ascii")

        else:
            transmission_data = data

        self.transport.write(transmission_data)

        print('Close the client socket')
        self.transport.close()


class sensors:
    def __init__(self):
        '''this will setup and store the instants sensor suit'''
        GPIO.setmode(GPIO.BCM)
        self._Window = Window()
        self._Temperature = HumidTemp()
        self._Motion = Motion()
        self._Sonics = Sonics()
        self._Sound = Sound()
        self.window: None|str = None
        self.temperature: None|float = None
        self.humidity: None|int = None
        self.motion: None|str = None
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
        self.sound_detection = self._Sound.detect()


    def dataFormatter(self):
        return json.dumps({
            "Wind": self.window,
            "Temp": self.temperature,
            "Humi": self.humidity,
            "Moti": self.motion,
            "Soni": self.door_distance,
            "Soun": self.sound_detection,
        })




default_port = 16576
Live_Sensors = sensors()

async def Node(address, port):
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        NodeServer,
        address, port)

    async with server:
        await server.serve_forever()

async def clockupdate(address=0x70):
    clock_display = S7.SevenSegment(address=address)
    clock_display.begin()
    while True:
        await asyncio.sleep(60)
        current_time =  str(datetime.now().hour)
        current_time += str(datetime.now().minute)
        clock_display.print_number_str(current_time)
        clock_display.write_display()



async def start_device():
    await asyncio.gather(
            Node(None, default_port),
            clockupdate()
            )
