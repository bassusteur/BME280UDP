# BME280UDP-micropython
I needed to send udp packets from my esp8266 to an InfluxDB database hosted on a raspberry pi so i stitched together some code and here it is for anyone who needs it.

## libraries used
I used this wonderful library by robert-hh:
https://github.com/robert-hh/BME280
i've uploaded an edited file taken from this library to get rid of the measurement units reported frm the bme.values function because influxdb didn't like them.
