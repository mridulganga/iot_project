from dht11 import read_temperature, read_humidity
from adc import read_ldr,read_gas

import requests
import time


# main loop
while(True):

    # get all sensor values and make a dict object
    sensor_values = {
        "temperature" : read_temperature(),
        "humidity" : read_humidity(),
        "gas" : read_gas(2),
        "ldr" : read_ldr(0)
    }

    # send all sensor values to server
    r = requests.post('https://localhost:8000/sensorvalues', data = sensor_values)
    
    # wait half a second
    time.sleep(0.5)