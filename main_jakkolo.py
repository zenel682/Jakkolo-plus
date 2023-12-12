from controller_jakkolo import App
from leaderboard_jakkolo import Leaderboard
from pages_jakkolo import leaderboard_pscores, leaderboard_pnames
import customtkinter as ctk

lb = Leaderboard()



def on_close():
    print("Close app")
    lb.safeAndCloseJSON(leaderboard_pnames, leaderboard_pscores)
    root.destroy()

def on_open():
    print("Executing code on window open")
    #lb.openAndReadJSON()


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", on_close)
    # Schedule the on_open function to run after a delay (e.g., 100 milliseconds)
    root.after(50, on_open)
    root.mainloop()

