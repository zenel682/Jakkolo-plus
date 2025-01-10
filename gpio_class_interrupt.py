import gpiod
import time
import threading

# Set GPIO pins for the buttons
button_pin_1 = 17
button_pin_2 = 27
button_pin_3 = 22
button_pin_4 = 23

button_line_1 = chip.get_line(button_pin_1)
button_line_1.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
class Endschalter:
    def __init__(self):
        print("EndschalterKlasse")
        
        # Configure GPIO lines
        self.chip = gpiod.Chip('gpiochip0')
        self.lines = self.chip.get_lines([button_pin_1, button_pin_2, button_pin_3, button_pin_4])
        self.lines.request(consumer="endschalter", type=gpiod.LINE_REQ_EV_FALLING_EDGE)
        
        self.read_it = True
        self.b1_counter = 0
        self.b2_counter = 0
        self.b3_counter = 0
        self.b4_counter = 0

    def stop(self):
        self.read_it = False
        self.lines.release()

    def button_pressed_callback(self, line_offset):
        if line_offset == button_pin_1:
            print("Button pressed 1")
            self.b1_counter += 1
        elif line_offset == button_pin_2:
            print("Button pressed 2")
            self.b2_counter += 1
        elif line_offset == button_pin_3:
            print("Button pressed 3")
            self.b3_counter += 1
        elif line_offset == button_pin_4:
            print("Button pressed 4")
            self.b4_counter += 1

    def read_endschalter(self, event: threading.Event):
        try:
            while not event.is_set():
                # Wait for an event on any of the lines
                events = self.lines.event_wait(sec=1)
                for event in events:
                    self.button_pressed_callback(event.line_offset)

        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            self.stop()

    def print_button_states(self):
        print("Button state 1:", self.b1_counter)
        print("Button state 2:", self.b2_counter)
        print("Button state 3:", self.b3_counter)
        print("Button state 4:", self.b4_counter)

if __name__ == "__main__":
    end = Endschalter()
    stop_event = threading.Event()
    try:
        thread = threading.Thread(target=end.read_endschalter, args=(stop_event,))
        thread.start()

        while True:
            time.sleep(5)  # Periodically print button states
            end.print_button_states()

    except KeyboardInterrupt:
        print("Stopping program...")
        stop_event.set()
        thread.join()
