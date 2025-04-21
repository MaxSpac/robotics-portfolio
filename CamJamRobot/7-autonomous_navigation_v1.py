# CamJam EduKit 3 - Robotics
# Worksheet 8 - Autonomous navigation V2

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library
from gpiozero import DistanceSensor 
from gpiozero import LED
import threading

led1 = LED(20)  # GPIO 20 for LED 1 (red)
led2 = LED(21)  # GPIO 24 for LED 2 (white)
led3 = LED(26)  # GPIO 26 fo LED3 (yellow-left)
led4 = LED(19)  # GPIO 19 for LED4 (yellow-right)



robot = CamJamKitRobot()

# Set the relative speeds of two motors, between 0.0 and 1.0
motorspeed = 0.3
leftmotorspeed=0.3
rightmotorspeed=0.3 # DCs not equally fast, now balanced
fastleft=0.6
fastright=0.93
slowleft = 0.15
slowright = 0.2325

motorforward = (leftmotorspeed, rightmotorspeed)
motorforwardfast = (fastleft, fastright)
motorforwardleft = (leftmotorspeed, fastright)
motorforwardright= (fastleft, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (-slowleft, fastright)
motorright = (fastleft, -rightmotorspeed)
motorstop = (0, 0)

# Define GPIO Pins to use for sensor
pinTriggerHigh = 17
pinEchoHigh = 18
pinTriggerLow = 27
pinEchoLow = 22

sensorHigh = DistanceSensor(echo=pinEchoHigh, trigger=pinTriggerHigh)
sensorLow = DistanceSensor(echo=pinEchoLow, trigger=pinTriggerLow)


# Initialisiere Sensor
print("Warm up sensor ...")
time.sleep(2)

# Distance variables
hownear = 35
reversetime = 1.5
turntime = 1

# LED function for right led
def right_led_blink(turntime, stop_blinking):
    end_time = time.time() + turntime  # Blink while turning
    while time.time() < end_time and not stop_blinking.is_set():
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        time.sleep(0.333)  # LED on
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.333)  # LED off
    led1.off()
    led2.off()
    led3.off()
    led4.off()  # Turn off LED 

# LED function for turning left

# Return True if sensor senses an obstacle
def is_near_obstacle(localhownear):
    distanceHigh = sensorHigh.distance * 100
    distanceLow = sensorLow.distance * 100
    

    # print("IsNearObstacle: " + str(distance))
    if distanceHigh < localhownear:
        print("High obstacle, distance: " + str(distanceHigh))
        return True
    if distanceLow < localhownear:
        print("Low obstacle, distance: " + str(distanceLow))
        return True
    else:
        return False

# Move back a little, then turn right:
def move_backwards():

    # Move back a little
    print("Backwards")
    led2.on()
    robot.value = motorbackward
    time.sleep(reversetime)
    led2.off()
    robot.value = motorstop
    
def turn_right():

    # Turn right
    print("Right")
    robot.value = motorright
    time.sleep(turntime)
    robot.value = motorstop

try:
    # Repeat the next intended block forever
    while True:
        
        led2.on()
        robot.value = motorforward
        time.sleep(0.1)
        #
       #robot.value = motorforwardleft
       #time.sleep(3)
       #robot.value = motorforwardright
       #time.sleep()
        if is_near_obstacle(hownear):
            led2.off()
            led1.on()
            robot.value = motorstop
            time.sleep(1)
            led1.off()
            move_backwards()
            led1.on()

            # Event to stop threads
            stop_blinking = threading.Event()

            # Threading events for parallel turning and blinking
            turn_right_thread = threading.Thread(target=turn_right)
            blink_right_thread = threading.Thread(target=right_led_blink, args=(turntime, stop_blinking))

            # Start threads
            turn_right_thread.start()
            blink_right_thread.start()

            # Pauses script til thread finished
            turn_right_thread.join()
            stop_blinking.set()
            blink_right_thread.join()

            print("Forward")


# press CTRL+C to cleanup and stop
except KeyboardInterrupt:
    robot.stop()
    

