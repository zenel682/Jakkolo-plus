# KeyListener.py
import keyboard
import time

class KeyListener:
    def __init__(self):
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0
        self.var4 = 0
        self.running = True

        # Register the callback for key presses
        keyboard.hook(callback=self.on_key_press)

    def on_key_press(self, e):
        if e.event_type == keyboard.KEY_DOWN:
            if e.name == '1':
                self.var1 += 1
            elif e.name == '2':
                self.var2 += 1
            elif e.name == '3':
                self.var3 += 1
            elif e.name == '4':
                self.var4 += 1

    def stop(self):
        self.running = False
        keyboard.unhook_all()

    def run(self):
        while self.running:
            time.sleep(0.1)  # Adjust the sleep time as needed
