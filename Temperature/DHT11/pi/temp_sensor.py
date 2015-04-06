import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

sensor_pin = 4

hum, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)

if hum is not None and temp is not None:
  print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum)
