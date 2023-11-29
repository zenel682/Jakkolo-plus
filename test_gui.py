import tkinter as tk
from tkinter import font

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Page Example")
        self.root.configure(bg="#E6E6FA")  # Set light purple background color

        # Set the default font for the buttons
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Helvetica", size=12, weight="bold")

        # Create normal style buttons
        self.start_button = tk.Button(
            root,
            text="Start",
            command=lambda: self.show_page("Start"),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.start_button.pack(ipadx=10, padx=20)

        self.add_hover_effect(self.start_button)

        self.leaderboard_button = tk.Button(
            root,
            text="Leaderboard",
            command=lambda: self.show_page("Leaderboard"),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.leaderboard_button.pack(ipadx=10, padx=20)
        self.add_hover_effect(self.leaderboard_button)

        self.explanation_button = tk.Button(
            root,
            text="Explanation",
            command=lambda: self.show_page("Explanation"),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.explanation_button.pack(ipadx=10, padx=20)
        self.add_hover_effect(self.explanation_button)

        # Frame to display content
        self.current_frame = tk.Frame(root, padx=20, pady=20, bg="#E6E6FA")  # Set light purple background color

    def add_hover_effect(self, button):
        button.bind("<Enter>", lambda event, b=button: self.on_enter(event, b))
        button.bind("<Leave>", lambda event, b=button: self.on_leave(event, b))

    def on_enter(self, event, button):
        button.config(bg="#FFD700")  # Brighter color on hover

    def on_leave(self, event, button):
        button.config(bg="#FFA500")  # Restore original color on leave

    def show_page(self, title):
        # Destroy any existing widgets in the current frame
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        # Display the title in the current frame
        title_label = tk.Label(self.current_frame, text=title, font=("Helvetica", 16, "bold"), bg="#E6E6FA")
        title_label.pack()

        # Button to go back to the main frame
        back_button = tk.Button(
            self.current_frame,
            text="Back to Main",
            command=self.show_main_page,
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        back_button.pack()

        self.add_hover_effect(back_button)

        # Hide the main buttons
        self.start_button.pack_forget()
        self.leaderboard_button.pack_forget()
        self.explanation_button.pack_forget()

        # Pack the current frame to display it
        self.current_frame.pack()

    def show_main_page(self):
        # Destroy any existing widgets in the current frame
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        # Re-display the original buttons in the main frame
        self.start_button.pack(ipadx=10, padx=20)
        self.leaderboard_button.pack(ipadx=10, padx=20)
        self.explanation_button.pack(ipadx=10, padx=20)

        # Unpack the current frame to hide it
        self.current_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
