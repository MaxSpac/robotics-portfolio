# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

robot.forward()
time.sleep(1)  # Pause for 1 second

robot.stop()