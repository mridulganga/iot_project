import requests
import time
from random import randint

# main loop
while(True):

    # generate sensor values for test
    sensor_values = {
        "temperature" : str(randint(1,200)),
        "humidity" : str(randint(1,100)),
        "gas" : str(randint(1,800)),
        "ldr" : str(randint(1,1000))
    }

    # send all sensor values to server
    r = requests.post('http://localhost:5000/sensorvalue', data = 
sensor_values)
    
    # wait half a second
    time.sleep(0.5)
