import RPi.GPIO as gp


class window:
    def __init__(self, pin: int = 19):
        gp.setup(pin, gp.IN)
        self.pin = pin

    def status(self):
        if gp.input(self.pin) == 1:
            return "open"
        else:
            return "closed"
