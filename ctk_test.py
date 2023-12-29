import tkinter as tk
from hudere_frame import HudereFrame

class HudereApp:
    def __init__(self, master):
        self.master = master
        master.title("Hudere")
        master.configure(bg="blue")  # Set background color of the root window
        master.overrideredirect(True)
        # Configure title bar color (may not work on all platforms)
        try:
            master.tk_setPalette(background="blue")
        except tk.TclError:
            pass

        # Set the icon (replace 'path/to/icon.png' with the actual path to your icon file)
        try:
            master.iconbitmap("icons\settings_icon.png")
        except tk.TclError:
            pass

        # Create the main frame
        self.main_frame = HudereFrame(master, "Main Frame", "pink")

        # Create a button to open a new frame
        open_frame_button = tk.Button(master, text="Open New Frame", command=self.open_new_frame, bg="blue", fg="white")
        open_frame_button.pack(pady=10)

    def open_new_frame(self):
        # Hide the main frame
        self.main_frame.frame.pack_forget()

        # Create a new frame with a different title and background color
        new_frame = HudereFrame(self.master, "New Frame", "green")

        # Create a button to go back to the main frame
        back_button = tk.Button(self.master, text="Back to Main", command=self.back_to_main, bg="blue", fg="white")
        back_button.pack(pady=10)

    def back_to_main(self):
        # Hide the new frame
        self.main_frame.frame.pack_forget()

        # Show the main frame
        self.main_frame.frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HudereApp(root)
    root.geometry("400x300")  # Set the size of the window
    root.mainloop()
