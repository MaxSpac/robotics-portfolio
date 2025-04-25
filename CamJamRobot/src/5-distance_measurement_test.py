# CamJam EduKit 3 - Robotics
# Worksheet 5 - Distance

import time  # Import the Time library
from gpiozero import DistanceSensor  # Import the GPIO Zero Library 

# Define GPIO pins to use on the Pi
pinTriggerHigh = 17
pinEchoHigh = 18
pinTriggerLow = 27
pinEchoLow = 22

sensorHigh = DistanceSensor(echo=pinEchoHigh, trigger=pinTriggerHigh)
sensorLow = DistanceSensor(echo=pinEchoLow, trigger=pinTriggerLow)

print("Ultrasonic Measurement")

try:
    #Repeat the next intended block forever
    while True:
        print("DistanceLow: %.lf cm" % (sensorHigh.distance *100))
        time.sleep(1)
        print("DistanceHigh: %.lf cm" % (sensorLow.distance * 100))
        time.sleep(1)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    exit()

