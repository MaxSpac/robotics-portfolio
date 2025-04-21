from gpiozero import LED
import time

led1 = LED(20)  # GPIO 20 for LED 1 (red)
led2 = LED(21)  # GPIO 24 for LED 2 (white)
led3 = LED(26)  # GPIO 26 fo LED3 (yellow-left)
led4 = LED(19)  # GPIO 19 for LED4 (yellow-right)

try:
    while True:
        led1.on()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(1)
        led1.off()
        led2.on()
        led3.off()
        led4.off()
        time.sleep(1)
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(1)
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        time.sleep(1)   # drei mal links blinken, dann drei mal rechts blinken, blink
        led1.off()
        led2.off()
        led3.on()
        led4.off()
        time.sleep(0.333) # aus
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.333) # blink
        led1.off()
        led2.off()
        led3.on()
        led4.off()
        time.sleep(0.333) # aus
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.333) # blink
        led1.off()
        led2.off()
        led3.on()
        led4.off()
        time.sleep(0.333) # aus
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.333) # blink
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        time.sleep(0.333) # aus
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.333) # blink
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        time.sleep(0.333) # aus
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(0.333) # blink
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        time.sleep(0.333) # aus
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        time.sleep(1)
        

except KeyboardInterrupt:
    led1.off()
    led2.off()
    led3.off()
    led4.off()