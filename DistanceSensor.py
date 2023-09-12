import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        distance = sonar.distance
        print("Distance:", distance)
        time.sleep(0.5)
    except RuntimeError:
        print("Retrying!")
        time.sleep(0.5)