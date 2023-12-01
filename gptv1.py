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

        # Set the window size and make it unscalable
        self.root.geometry("1024x600")
        self.root.resizable(False, False)

        # Frame to display content
        self.current_frame = tk.Frame(root, padx=20, pady=20, bg="#E6E6FA")  # Set light purple background color

        # Create square buttons for player selection
        self.create_player_buttons()

        # Create rectangular buttons below the square buttons
        self.create_rectangular_buttons()

        # Create a smaller square button with an image
        self.create_image_button()

    def create_player_buttons(self):
        players = ["Singleplayer", "2 Spieler", "3 Spieler", "4 Spieler"]
        frame_player_buttons = tk.Frame(self.root, bg="#E6E6FA")
        for player in players:
            player_button = tk.Button(
                frame_player_buttons,
                text=player,
                command=lambda p=player: self.show_page("Player Selection", p),
                bg="#FFA500",
                fg="white",
                font=("Helvetica", 12, "bold"),
                width=10, height=2  # Square button
            )
            player_button.pack(side=tk.LEFT, padx=10)
            self.add_hover_effect(player_button)
        frame_player_buttons.pack(side=tk.TOP, pady=10)

    def create_rectangular_buttons(self):
        rectangular_buttons = ["Start", "Anleitung", "Bestenliste"]
        frame_rectangular_buttons = tk.Frame(self.root, bg="#E6E6FA")
        for button_text in rectangular_buttons:
            rectangular_button = tk.Button(
                frame_rectangular_buttons,
                text=button_text,
                command=lambda b=button_text: self.show_page("Rectangular Buttons", b),
                bg="#FFA500",
                fg="white",
                font=("Helvetica", 12, "bold"),
                width=20, height=2  # Rectangular button
            )
            rectangular_button.pack(pady=10)
            self.add_hover_effect(rectangular_button)
        frame_rectangular_buttons.pack(side=tk.TOP, pady=10)

    def create_image_button(self):
        # Create a PhotoImage object from an image file
        image = tk.PhotoImage(file="gear.png")

        image_button = tk.Button(
            self.root,
            image=image,
            command=lambda: self.show_page("Image Button", "Image Button"),
            bg="#FFA500",
            width=50, height=50  # Smaller square button
        )
        image_button.image = image  # Retain a reference to the image to prevent garbage collection
        image_button.pack(side=tk.TOP, pady=10)
        self.add_hover_effect(image_button)

    def add_hover_effect(self, button):
        button.bind("<Enter>", lambda event, b=button: self.on_enter(event, b))
        button.bind("<Leave>", lambda event, b=button: self.on_leave(event, b))

    def on_enter(self, event, button):
        button.config(bg="#FFD700")  # Brighter color on hover

    def on_leave(self, event, button):
        button.config(bg="#FFA500")  # Restore original color on leave

    def show_page(self, page_title, button_text):
        # Destroy any existing widgets in the current frame
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        # Display the title in the current frame
        title_label = tk.Label(self.current_frame, text=page_title, font=("Helvetica", 16, "bold"), bg="#E6E6FA")
        title_label.pack()

        # Display the selected button's text
        selected_button_label = tk.Label(self.current_frame, text=f"Selected Button: {button_text}", font=("Helvetica", 14), bg="#E6E6FA")
        selected_button_label.pack(pady=10)

        # Button to go back to the main page
        back_button = tk.Button(
            self.current_frame,
            text="Back to Main",
            command=self.show_main_page,
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=20, height=2  # Rectangular button
        )
        back_button.pack()

        self.add_hover_effect(back_button)

        # Pack the current frame to display it
        self.current_frame.pack()

    def show_main_page(self):
        # Destroy any existing widgets in the current frame
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        # Re-display the original buttons in the main frame
        self.create_player_buttons()
        self.create_rectangular_buttons()
        self.create_image_button()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
