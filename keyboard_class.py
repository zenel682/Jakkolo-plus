import keyboard
import time
import threading

class KeyCounter:
    def __init__(self, stop_flag):
        # Initialize variables
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0
        self.var4 = 0
        self.readKeys = True
        self.stop_flag = stop_flag

        # Register the callback for key releases
        keyboard.on_release(callback=self.on_key_release)

    def on_key_release(self, e):
        if e.name == '1':
            self.var1 += 1
        elif e.name == '2':
            self.var2 += 1
        elif e.name == '3':
            self.var3 += 1
        elif e.name == '4':
            self.var4 += 1

        # Print the values of the variables
        self.print_variables()

    def print_variables(self):
        print(f'var1: {self.var1}, var2: {self.var2}, var3: {self.var3}, var4: {self.var4}')

    def run(self, stop_flag):
        while not stop_flag.is_set():
            time.sleep(0.1)
            """try:
                # Keep the script running
                keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
            except KeyboardInterrupt:
                print("Exit")
                self.readKeys = False
            finally:
                # Unregister the callback to avoid memory leaks
                self.readKeys = False
                keyboard.unhook_all()"""

    def stop(self):
        self.readKeys = False
        keyboard.unhook_all()

if __name__ == "__main__":
    stop_flag = threading.Event()
    kc = KeyCounter(stop_flag=stop_flag)
    kc.run(stop_flag=stop_flag)