# MyApp.py
import tkinter as tk
from threading import Thread
from KeyListener import KeyListener

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Press Listener")

        self.label_var = tk.StringVar()
        self.label_var.set("Press Start to track key presses.")

        self.label = tk.Label(root, textvariable=self.label_var, font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_listening)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_listening)
        self.stop_button.pack()

        self.key_listener_thread = None

    def start_listening(self):
        self.key_listener_thread = Thread(target=self.run_key_listener)
        self.key_listener_thread.start()

    def run_key_listener(self):
        self.label_var.set("Listening to key presses...")
        key_listener = KeyListener()
        key_listener.run()

    def stop_listening(self):
        if self.key_listener_thread and self.key_listener_thread.is_alive():
            self.key_listener_thread.join()  # Wait for the thread to finish
        self.label_var.set("Press Start to track key presses.")
