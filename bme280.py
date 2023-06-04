import network, os, time
import usocket as socket
from machine import Pin, I2C
import bme280_float as bme280

localIP = "youresp'sip"
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
        wlan.connect('SSID', 'PASSWORD')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig()
do_connect()

s.connect(("targetip",targetport))

#define value strings
temp_str = ""
pr_str = ""
hum_str = ""

temp_str, pr_str, hum_str = bme.values #unpacks bme.values

msg = "BME280 temperature={},pressure={},humidity={}".format(*bme.values)

while(True):
  s.send(msg) #this sends our message with all the data
  time.sleep(1) #time in between each packet is sent (sleep() is in seconds)


