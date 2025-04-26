from gpiozero import CamJamKitRobot, DistanceSensor, LED

class HardwareInterface:
    def __init__(self):

        # LEDs
        self.led_red = LED(20)
        self.led_white = LED(21)
        self.led_yellow_left = LED(26)
        self.led_yellow_right = LED(19)

        # Robot
        self.robot = CamJamKitRobot

        # Sensors
        self.sensor_high = DistanceSensor(echo=18, trigger=17)
        self.sensor_low = DistanceSensor(echo=22, trigger=27)

        # Set motor speed
    def set_motor_speed(self, left_speed, right_speed):
        self.robot.value = (left_speed, right_speed)

    def stop_robot(self):
        # Stop robot
        self.robot.value = (0, 0)

        
    def get_distances(self):
        # Get distances from sensors in cm
        return {
            "low": self.sensor_low.distance * 100,
            "high": self.sensor_high.distance * 100
                }
    
    def set_led_state(self, led_name, state):
        # Switch LED on or off
        led = getattr(self, f"led_{led_name}")
        if state:
            led.on()
        else:
            led.off()




