##
# Siple example program to control RGB led (please check the right amount of resistor required for your hardware in the doc provided with this sample code) 
# 
# Devloper info : 
# Ehanno Maxime / ehanno.dev@gmail.com / https://github.com/Sora-141
# 
# feel free to contact me if you have anny question(s).
##

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

RedPin = 17
GreenPin = 27
BluePin = 22

# seting up the RPI GPIO
GPIO.setup(RedPin, GPIO.OUT)
GPIO.setup(GreenPin, GPIO.OUT)
GPIO.setup(BluePin, GPIO.OUT)

RedLed = GPIO.PWM(RedPin, 100)
RedLed.start(0)
GreenLed = GPIO.PWM(GreenPin, 100)
GreenLed.start(0)
BlueLed = GPIO.PWM(BluePin, 100)
BlueLed.start(0)


def LedCicle(Led):
    #sloly turnn it on
    for x in range(100):
        Led.ChangeDutyCycle(x)
        sleep(0.01)
    Led.ChangeDutyCycle(100)

    #sloly turnn it off
    for x in range(100,0,-1):
        Led.ChangeDutyCycle(x)
        sleep(0.01)
    Led.ChangeDutyCycle(0)

try:
    while True:
        LedCicle(RedLed)
        LedCicle(GreenLed)
        LedCicle(BlueLed)
except KeyboardInterrupt:
    GPIO.cleanup()