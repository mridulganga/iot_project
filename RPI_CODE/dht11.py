import Adafruit_DHT

dht_sensor = Adafruit_DHT.DHT11

# Change this later
dht_gpio = 17


def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_gpio)
    if temperature is not None:
        return temperature


def read_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_gpio)
    if humidity is not None:
        return humidity



# testing code

if __name__=="__main__":
    while True:
        print("TEMP : " + read_temperature())
        print("HUMIDITY : " + read_humidity())


# Formatting Code
# if humidity is not None and temperature is not None:
#     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
# else:
#     print('Failed to get reading. Try again!')
