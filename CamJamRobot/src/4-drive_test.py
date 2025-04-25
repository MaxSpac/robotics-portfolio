# CamJam EduKit 3 - Robotics
# Worksheet 4 - Driving

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

robot.forward()
time.sleep(1.5) 

robot.right()
time.sleep(0.5)

robot.forward()
time.sleep(2) 

robot.left()
time.sleep(3)

robot.stop()