import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set the GPIO pin for the button
button_pin_1 = 35
button_pin_2 = 36
button_pin_3 = 37
button_pin_4 = 38
global read_it


class Endschalter:
    def __init__(self, stop_flag):
        # Setup the GPIO pin as an input with a pull-up resistor
        GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(button_pin_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.read_it = True
        self.stop_flag = stop_flag
        self.bs1_old = 1
        self.bs2_old = 1
        self.bs3_old = 1
        self.bs4_old = 1
        self.b1_counter = 0
        self.b2_counter = 0
        self.b3_counter = 0
        self.b4_counter = 0
    def stop(self):
        self.read_it = False
        GPIO.cleanup()
    
    def read_endschalter(self, stop_flag):
        try:
            while not stop_flag.is_set():
                # Read the state of the button
                button_state_1 = GPIO.input(button_pin_1)
                button_state_2 = GPIO.input(button_pin_2)
                button_state_3 = GPIO.input(button_pin_3)
                button_state_4 = GPIO.input(button_pin_4)

                # Add 1 if state changes
                if self.bs1_old != button_state_1 and button_state_1 == 1:
                    self.b1_counter += 1
                if self.bs2_old != button_state_2 and button_state_2 == 1:
                    self.b2_counter += 1
                if self.bs3_old != button_state_3 and button_state_3 == 1:
                    self.b3_counter += 1
                if self.bs4_old != button_state_4 and button_state_4 == 1:
                    self.b4_counter += 1
           
            
                # Print the state
                print("Button state 1:", button_state_1, self.b1_counter)
                print("Button state 2:", button_state_2, self.b2_counter)
                print("Button state 3:", button_state_3, self.b3_counter)
                print("Button state 4:", button_state_4, self.b4_counter)
                # Add a delay to avoid rapid readings
                time.sleep(0.1)
                
                # Update old values
                self.bs1_old = button_state_1
                self.bs2_old = button_state_2
                self.bs3_old = button_state_3
                self.bs4_old = button_state_4

        except KeyboardInterrupt:
            print("Exiting...")

            
#if __name__ == "__main__":
#    end = Endschalter()
#    end.read_endschalter()
