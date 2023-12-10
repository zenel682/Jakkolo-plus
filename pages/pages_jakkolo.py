import customtkinter as ctk

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent

        self.label = ctk.CTkLabel(self, text="Mainpage")
        self.label.pack(padx=20, pady=20)
        self.button = ctk.CTkButton(self, text="Go to Page 2", command=lambda: switch_callback(AnleitungsFrame))
        self.button.pack(pady=10)

class AnleitungsFrame(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Anleitung")
        self.label2.pack(pady=20)
        self.button = ctk.CTkButton(self, text="Return to Page 1", command=lambda: switch_callback(MainPage))
        self.button.pack(pady=10)
