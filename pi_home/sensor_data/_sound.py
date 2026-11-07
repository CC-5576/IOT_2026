import RPi.GPIO as gp
from time import sleep, time


class sound:
    """
    this will be used to return if there is noise from the microphone
    default microphone pin is 24, change with pin=00
    default microphone sensitivity is set to an average of 0.05 over a 30 second window.
        to adjust you can either adjust the microphone it's self, or the average in software.
        this average is changeable by calling this function with avg=0.00
    """

    def __init__(self, pin=24, avg=0.05):
        gp.setmode(gp.BCM)
        gp.setup(pin, gp.IN, pull_up_down=gp.PUD_UP)
        self.pin = pin
        self.avg = 0.05

    def detect(self):
        et = time() + 30
        noise_detection = []
        while time() < et:
            noise_detection.append(gp.input(self.pin))
        avg = sum(noise_detection) / len(noise_detection)
        print(avg, len(noise_detection))
        if avg <= self.avg:
            return "no noise detected"
        elif avg > self.avg:
            return "noise detected"
        # based on a testing, an average greater than 0.1
