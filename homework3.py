import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 17
GPIO.setup(led1,GPIO.OUT)
led2 = 18
GPIO.setup(led2,GPIO.OUT)
led3 = 27
GPIO.setup(led3,GPIO.OUT)
buzzer = 22
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(led1,0)
GPIO.output(led2,0)
GPIO.output(led3,1)
GPIO.output(buzzer,0)

while True:
    try:
        #1
        GPIO.output(led1,1)
        GPIO.output(led2,0)
        GPIO.output(led3,0)
        sleep(60)
        #2
        GPIO.output(led1,0)
        GPIO.output(led2,0)
        GPIO.output(led3,0)
        for i in range(5):
            GPIO.output(led2,1)
            GPIO.output(buzzer,1)
            sleep(1)
            GPIO.output(led2,0)
            GPIO.output(buzzer,0)
            sleep(1)
        #3
        GPIO.output(led1,0)
        GPIO.output(led2,0)
        GPIO.output(led3,1)
        GPIO.output(buzzer,0)
        sleep(60)
        #4
        GPIO.output(led1,0)
        GPIO.output(led2,0)
        GPIO.output(led3,0)
        for i in range(3):
            GPIO.output(led2,1)
            GPIO.output(buzzer,1)
            sleep(1)
            GPIO.output(led2,0)
            GPIO.output(buzzer,0)
            sleep(1)
    except:
        GPIO.cleanup()
