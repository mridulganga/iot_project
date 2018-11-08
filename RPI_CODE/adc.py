import spidev
import time


#Define Variables
delay = 0.5
ldr_channel = 0
gas_channel = 2

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)


def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def read_ldr(adcpin=0):
    return readadc(adcpin)

def read_gas(adcpin=2):
    return readadc(adcpin)



# Testing Code
if __name__=="__main__":

    while True:
        ldr_value = readadc(ldr_channel)
        gas_value = readadc(gas_channel)
        print("Gas Value: " + str(gas_value))
        print("LDR Value: " + str(ldr_value))
        time.sleep(delay)