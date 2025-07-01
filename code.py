from adafruit_circuitplayground import cp
import time

def pixels_on():
    for i in range(10):
        cp.pixels[i] = (50, 50, 50)

def pixels_off():
    for i in range (10):
        cp.pixels[i] = (0, 0, 0)

while True:
    if  cp.touch_A1:
        pixels_on()
    else:
        pixels_off()

        time.sleep(0.05)
