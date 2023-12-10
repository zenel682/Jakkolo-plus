import tkinter as tk
import threading
import time

class CounterThread(threading.Thread):
    def __init__(self, label):
        super().__init__()
        self.label = label
        self.running = threading.Event()

    def run(self):
        count = 0
        while self.running.is_set():
            time.sleep(1)
            count += 1
            self.label.config(text=f"Count: {count}")
            self.label.update_idletasks()  # Update the label in the main thread

    def stop(self):
        self.running.clear()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Thread Control Example")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="Count: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(
            root,
            text="Start Thread",
            command=self.start_thread,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.start_button.pack(ipadx=10, pady=10)

        self.stop_button = tk.Button(
            root,
            text="Stop Thread",
            command=self.stop_thread,
            bg="#FF0000",
            fg="white",
            font=("Helvetica", 12, "bold"),
            state=tk.DISABLED,
        )
        self.stop_button.pack(ipadx=10, pady=10)

    def start_thread(self):
        if not hasattr(self, 'thread') or not self.thread.is_alive():
            self.thread = CounterThread(self.label)
            self.thread.start()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.root.after(100, self.update_label)  # Schedule label update

    def stop_thread(self):
        if hasattr(self, 'thread') and self.thread.is_alive():
            self.thread.stop()
            self.thread.join()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_label(self):
        if hasattr(self, 'thread') and self.thread.is_alive():
            self.label.config(text=f"Count: {self.thread.label['text']}")
            self.root.after(100, self.update_label)  # Schedule next update

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
