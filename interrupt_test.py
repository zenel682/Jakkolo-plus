
import signal
import sys
import RPi.GPIO as GPIO

BUTTON_GPIO1 = 35
BUTTON_GPIO2 = 36
BUTTON_GPIO3 = 37
BUTTON_GPIO4 = 38
button = "00"

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_pressed_callback1(channel):
    print("Button pressed 1")

def button_pressed_callback2(channel):
    print("Button pressed 2")

def button_pressed_callback3(channel):
    print("Button pressed 3")

def button_pressed_callback4(channel):
    print("Button pressed 4")
    
def readButtons():
    GPIO.add_event_detect(BUTTON_GPIO1, GPIO.FALLING, 
            callback=button_pressed_callback1, bouncetime=50)
    GPIO.add_event_detect(BUTTON_GPIO2, GPIO.FALLING, 
            callback=button_pressed_callback2, bouncetime=50)
    GPIO.add_event_detect(BUTTON_GPIO3, GPIO.FALLING, 
            callback=button_pressed_callback3, bouncetime=50)
    GPIO.add_event_detect(BUTTON_GPIO4, GPIO.FALLING, 
            callback=button_pressed_callback4, bouncetime=50)
    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_GPIO1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_GPIO2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_GPIO3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_GPIO4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    readButtons()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
"""
import RPi.GPIO as GPIO

BUTTON_GPIO = 35

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING)
        print("Button pressed!")
"""
