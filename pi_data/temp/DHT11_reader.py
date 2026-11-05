import board
import adafruit_dht as dht

sensor = dht.DHT11(board.D4)
temp = sensor.temperature
humi = sensor.humidity

print(temp, humi)
