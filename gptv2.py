import tkinter as tk
from tkinter import font

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Spielauswahl")
        self.geometry("1024x600")
        self.resizable(False, False)

        # Create a background frame
        self.background_frame = tk.Frame(self, bg="#87CEFA")
        self.background_frame.pack(fill=tk.BOTH, expand=True)

        # Create a title label
        title_label = tk.Label(self.background_frame, text="Spielauswahl", font=("Arial", 24), bg="#87CEFA", fg="#FFFFFF")
        title_label.pack(side=tk.TOP, pady=20)

        # Create normal style buttons
        buttons_data = [
            ("Singleplayer", self.open_singleplayer_page),
            ("2 Spieler", self.open_zwei_spieler_page),
            ("3 Spieler", self.open_drei_spieler_page),
            ("4 Spieler", self.open_vier_spieler_page),
            ("Start", self.open_start_page),
            ("Anleitung", self.open_anleitung_page),
            ("Bestenliste", self.open_bestenliste_page),
        ]

        for button_text, command_function in buttons_data:
            button = tk.Button(
                self.background_frame,
                text=button_text,
                bg="#6495ED",
                fg="#FFFFFF",
                font=("Arial", 14),
                command=lambda func=command_function, text=button_text: self.open_new_page(func, text)
            )
            button.pack(side=tk.TOP, pady=10)

    def open_new_page(self, command_function, button_text):
        # Destroy any existing widgets in the background frame
        for widget in self.background_frame.winfo_children():
            widget.destroy()

        # Display the title in the background frame
        title_label = tk.Label(self.background_frame, text=button_text, font=("Arial", 16, "bold"), bg="#87CEFA", fg="#FFFFFF")
        title_label.pack()

        # Button to go back to the main frame
        back_button = tk.Button(
            self.background_frame,
            text="Back to Main",
            command=self.show_main_page,
            bg="#CC6699",
            fg="#FFFFFF",
            font=("Arial", 14),
        )
        back_button.pack(side=tk.BOTTOM, pady=20)

        # Pack the background frame to display it
        self.background_frame.pack()

        # Execute the specific function for the button
        command_function()

    def show_main_page(self):
        # Destroy any existing widgets in the background frame
        for widget in self.background_frame.winfo_children():
            widget.destroy()

        # Re-display the original buttons in the background frame
        self.__init__()

    def open_singleplayer_page(self):
        print("Singleplayer page")

    def open_zwei_spieler_page(self):
        print("2 Spieler page")

    def open_drei_spieler_page(self):
        print("3 Spieler page")

    def open_vier_spieler_page(self):
        print("4 Spieler page")

    def open_start_page(self):
        print("Start page")

    def open_anleitung_page(self):
        print("Anleitung page")

    def open_bestenliste_page(self):
        print("Bestenliste page")

if __name__ == "__main__":
    app = App()
    app.mainloop()
