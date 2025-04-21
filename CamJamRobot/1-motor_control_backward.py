# CamJam EduKit 3 - Robotics
# Backwards

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

robot.backward()
time.sleep(1)

robot.stop()