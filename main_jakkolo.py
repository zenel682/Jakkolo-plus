from controller_jakkolo import App, Leaderboard
import customtkinter as ctk

lb = Leaderboard()

def on_close():
    print("Close app")
    #lb.safeAndCloseJSON()
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

