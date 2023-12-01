import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Spielauswahl")
        self.geometry("500x500")

        # Set the window size and make it unscalable
        self.geometry("1024x600")
        self.resizable(False, False)

        # Create a background frame
        background_frame = tk.Frame(self, bg="#87CEFA")
        background_frame.pack(fill=tk.BOTH, expand=True)

        # Create a title label
        title_label = tk.Label(background_frame, text="Spielauswahl", font=("Arial", 24), bg="#87CEFA", fg="#FFFFFF")
        title_label.pack(side=tk.TOP, pady=20)

        # Create a Singleplayer button
        singleplayer_button = tk.Button(background_frame, text="Singleplayer", bg="#6495ED", fg="#FFFFFF", font=("Arial", 14), command=self.open_singleplayer_page)
        singleplayer_button.pack(side=tk.TOP, pady=10)

        # Create a 2 Spieler button
        zwei_spieler_button = tk.Button(background_frame, text="2 Spieler", bg="#6495ED", fg="#FFFFFF", font=("Arial", 14), command=self.open_zwei_spieler_page)
        zwei_spieler_button.pack(side=tk.TOP, pady=10)

        # Create a 3 Spieler button
        drei_spieler_button = tk.Button(background_frame, text="3 Spieler", bg="#6495ED", fg="#FFFFFF", font=("Arial", 14), command=self.open_drei_spieler_page)
        drei_spieler_button.pack(side=tk.TOP, pady=10)

        # Create a 4 Spieler button
        vier_spieler_button = tk.Button(background_frame, text="4 Spieler", bg="#6495ED", fg="#FFFFFF", font=("Arial", 14), command=self.open_vier_spieler_page)
        vier_spieler_button.pack(side=tk.TOP, pady=10)

        # Create a Start button
        start_button = tk.Button(background_frame, text="Start", bg="#CC6699", fg="#FFFFFF", font=("Arial", 14), command=self.open_start_page)
        start_button.pack(side=tk.BOTTOM, pady=20)

        # Create an Anleitung button
        anleitung_button = tk.Button(background_frame, text="Anleitung", bg="#CC6699", fg="#FFFFFF", font=("Arial", 14), command=self.open_anleitung_page)
        anleitung_button.pack(side=tk.BOTTOM, pady=20)

        # Create a Bestenliste button
        bestenliste_button = tk.Button(background_frame, text="Bestenliste", bg="#CC6699", fg="#FFFFFF", font=("Arial", 14), command=self.open_bestenliste_page)
        bestenliste_button.pack(side=tk.BOTTOM, pady=20)

    # Define functions to open new pages
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
