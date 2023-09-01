#Libraries
#import time	#https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit	#https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from time import sleep



kit=ServoKit(channels=16)
servo=14
while True:
    a=input("Enter Any Angle Degree (0-180):")
    for i in range(servo):
        print (i)
        kit.servo[i].angle=int(a)

