import time 
import RPi.GPIO as io 
io.setmode(io.BCM) 
 
power_pin = 24
 
io.setup(power_pin, io.OUT)
io.output(power_pin, False)
print("POWER ON")
io.output(power_pin, True)
