import RPi.GPIO as GPIO
import time
import atexit
def what_do():		
	GPIO.output(out_pin,False)
	exit	
atexit.register(what_do)
sec=1
GPIO.setmode(GPIO.BOARD)
out_pin=35
in_pin=11
GPIO.setup(out_pin,GPIO.OUT)
GPIO.setup(in_pin,GPIO.IN)
while True:
	value=GPIO.input(in_pin)
	if value==False:
		GPIO.output(out_pin,True)
		time.sleep(sec)
		GPIO.output(out_pin,False)
		time.sleep(0.2*sec)
	if value==True:	
		GPIO.output(out_pin,True)
		time.sleep(0.1*sec)
