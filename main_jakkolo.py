from controller_jakkolo import App
from leaderboard_jakkolo import Leaderboard
from pages_jakkolo_raspi import lb_pnames_pscores
import customtkinter as ctk

lb = Leaderboard()

def on_close():
    print("Close app")
    lb.safeAndCloseJSON(lb_pnames_pscores)
    root.destroy()

def on_open():
    print("Executing code on window open")

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    # Schedule the on_open function to run after a delay (e.g., 100 milliseconds)
    root.after(50, on_open)
    root.mainloop()
