# CamJam EduKit 3 - Robotics
# Worksheet 6 - Controlling speed with Pulse-Width-Modulation

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

robot = CamJamKitRobot()

# Set the relative speeds of two motors, between 0.0 and 1.0
motorspeed = 0.3
leftmotorspeed=0.3
rightmotorspeed=0.465
fastleft=0.6
fastright=0.93

motorforward = (leftmotorspeed, rightmotorspeed)
motorforwardfast= (fastleft, fastright)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, -rightmotorspeed)
motorright = (-leftmotorspeed, rightmotorspeed)
motorstop = (0, 0)

time.sleep(2)

robot.value = motorforward
time.sleep(2) 

robot.value = motorstop
time.sleep(0.5)

robot.value = motorright
time.sleep(3.5)

robot.value = motorstop
time.sleep(0.5)

robot.value = motorforwardfast
time.sleep(2)

robot.value = motorstop
time.sleep(0.5)

robot.value = motorleft
time.sleep(3.5)


robot.stop()