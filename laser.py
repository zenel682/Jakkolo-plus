import RPi.GPIO as GPIO

laserpin = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(laserpin, GPIO.OUT)

def startLaser():
	print("ON")
	GPIO.output(laserpin, GPIO.HIGH)

def stopLaser():
	print("OFF")
	GPIO.output(laserpin, GPIO.LOW)
