from rainbowio import colorwheel
#import neopixel
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)

while True:
    try:
        print((sonar.distance,))
        if (sonar.distance < 5):
             print("less than 5")
        if (sonar.distance > 5):
             print("less than 5")     
        if (sonar.distance > 5):
             print("more than 5")  
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    