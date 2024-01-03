import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins
input_pin = 7
output_pin = 24

# Set up input pin with pull-down resistor
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set up output pin
GPIO.setup(output_pin, GPIO.OUT)

try:
    while True:
        # Read the state of the input pin
        input_state = GPIO.input(input_pin)

        # Check if the button is pressed
        if input_state == GPIO.HIGH:
            print("Button is pressed. Turning on the output.")
            GPIO.output(output_pin, GPIO.HIGH)
        else:
            print("Button is not pressed. Turning off the output.")
            GPIO.output(output_pin, GPIO.LOW)

        # Add a small delay to debounce and prevent rapid toggling
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
