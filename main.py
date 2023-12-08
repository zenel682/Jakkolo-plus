import tkinter as tk
import atexit
from app_threaded import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    # Register cleanup function
    atexit.register(app.stop_threads)
    root.mainloop()