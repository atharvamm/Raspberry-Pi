import RPi.GPIO as GPIO
import time
import atexit
def what_do():		
	GPIO.output(pwm_pin,False)
	exit	
atexit.register(what_do)
GPIO.setmode(GPIO.BOARD)
pwm_pin=12
GPIO.setup(pwm_pin,GPIO.OUT)
pwm=GPIO.PWM(pwm_pin,50)
pwm.start(0)
while True:
	time.sleep(1)
	for i in range(20):
		pwm.ChangeDutyCycle(i)
		time.sleep(0.1)
	time.sleep(2)
	for i in range(20,0,-1):
		pwm.ChangeDutyCycle(i)
		time.sleep(0.1)
	#GPIO.output(pwm_pin,False)	  
