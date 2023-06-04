import network, os, time
import usocket as socket
from machine import Pin, I2C
import bme280_float as bme280

localIP = "10.0.0.11"
localPort = 8888

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
bme = bme280.BME280(i2c=i2c)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((localIP, localPort))

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('enel-WiFi_5C322CE1', 'TR7RXN7QQC')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


do_connect()
s.connect(("10.0.0.7",8089))

temp_str = ""
pr_str = ""
hum_str = ""

temp_str, pr_str, hum_str = bme.values

msg = "BME280 temperature={},pressure={},humidity={}".format(*bme.values)

while(True):
  s.send(msg)
  time.sleep(1)


