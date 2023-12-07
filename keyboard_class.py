import keyboard

class KeyCounter:
    def __init__(self):
        # Initialize variables
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0
        self.var4 = 0
        self.readKeys = True

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

    def run(self):
        while self.readKeys:
            try:
                # Keep the script running
                keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
            except KeyboardInterrupt:
                print("Exit")
                self.readKeys = False
            finally:
                # Unregister the callback to avoid memory leaks
                keyboard.unhook_all()

    def stop(self):
        self.readKeys = False
        keyboard.unhook_all()