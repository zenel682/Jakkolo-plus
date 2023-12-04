import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for the button
button_pin = 17

# Setup the GPIO pin as an input with a pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Read the state of the button
        button_state = GPIO.input(button_pin)

        # Print the state
        print("Button state:", button_state)

        # Add a delay to avoid rapid readings
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Cleanup GPIO settings
    GPIO.cleanup()
