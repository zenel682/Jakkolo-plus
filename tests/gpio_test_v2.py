import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set the GPIO pin for the button
button_pin_1 = 35
button_pin_2 = 36
button_pin_3 = 37
button_pin_4 = 38

# Setup the GPIO pin as an input with a pull-up resistor
GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        # Read the state of the button
        button_state_1 = GPIO.input(button_pin_1)
        button_state_2 = GPIO.input(button_pin_2)
        button_state_3 = GPIO.input(button_pin_3)
        button_state_4 = GPIO.input(button_pin_4)

        # Print the state
        print("Button state 1:", button_state_1)
        print("Button state 2:", button_state_2)
        print("Button state 3:", button_state_3)
        print("Button state 4:", button_state_4)
        # Add a delay to avoid rapid readings
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Cleanup GPIO settings
    GPIO.cleanup()
