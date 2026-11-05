import RPi.GPIO as GP
import time

m_pin = 23
GP.setmode(GP.BCM)
GP.setup(m_pin, GP.IN)

while 1:
    if GP.input(m_pin) == 0:
        print("No motion")
    elif GP.input(m_pin) == 1:
        print("motion!!!!!!!!!!!")
    time.sleep(1)

