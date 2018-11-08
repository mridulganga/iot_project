### Hardware Components Needed for Project
1. Rasoberry Pi 3B+
2. MCP3008 (ADC Module)
3. DHT 11 (Temprature and Humidity Sensor)
4. MQ135 (Gas Sensor Module)
5. LDR


### Using ADC in RPi

![Rpi ADC](https://cdn.pimylifeup.com/wp-content/uploads/2016/05/Raspberry-Pi-ADC-Circuit.png)


#### Circuit Connections

ADC Channels in use
0 - LDR  
2 - GAS


### Install DHT Library 

open terminal on raspberry pi  
then run 
```
sudo pip3 install Adafruit_DHT
```
to install the Adafruit DHT Library which is being used int he project.
