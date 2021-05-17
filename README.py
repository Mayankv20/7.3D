# 7.3D
import RPi.GPIO as IO
import time
from gpiozero import DistanceSensor
from time import sleep

IO.setmode(IO.BOARD)
IO.setwarnings(False)

IO.setup(8,IO.OUT)

p = IO.PWM(8,100)
sensor = DistanceSensor(trigger=18, echo=24)

p.start(0)
while True:
     sleep(1.5)
     
     distance = round(sensor.distance*100, 2)
     
     if(distance < 50):
         p.ChangeDutyCycle(100-(distance*2))
    
     else:
         p.ChangeDutyCycle(0)
     print("Distance: {}".format(distance))
