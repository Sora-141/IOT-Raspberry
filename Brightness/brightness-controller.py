############################
#!/usr/bin/python3
# Simple LED brightness controller
# using RaspberryPy BCM pins (https://pinout.xyz/pinout/)
# float brightness value betwen 0.0 and 250.0
# author informations : https://github.com/Sora-141 | ehanno.dev@gmail.com | https://www.linkedin.com/in/maxime-ehanno/
#########
# manual testing
## $sudo pigpiod  -> Starts PiGPIO
## $pigs p 17 0 -> The brightness of pin 17 is set to 0% 
## $pigs p 17 255 -> The brightness of pin 17 is set to 100% 
############################

import time
import pigpio

pi = pigpio.pi()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ValueInBoud(value: float):
    if value > 255.0:
        print(bcolors.WARNING + "[!] brightnes must be betwen 0 and 255" + bcolors.ENDC)
        print("[i] seting brightnes to : 255")
        return 255.0
    if value < 0.0:
        print(bcolors.WARNING + "[!] brightnes must be betwen 0 and 255" + bcolors.ENDC)
        print("[i] seting brightnes to : 0")
        return 0.0
    return value


def SetLight(BCMpin: int, brightness: float):
    value = ValueInBoud(brightness)
    pi.set_PWM_dutycycle(BCMpin, value)
