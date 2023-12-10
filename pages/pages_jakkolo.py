import customtkinter as ctk

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent

        self.label = ctk.CTkLabel(self, text="Mainpage")
        self.label.pack(padx=20, pady=20)
        self.explain_button = ctk.CTkButton(self, text="Anleitung", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10)
        self.leaderboard_button = ctk.CTkButton(self, text="Bestenliste", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10)
        self.start_button = ctk.CTkButton(self, text="Start", command=lambda: switch_callback(SpielernamenPage))
        self.start_button.pack(pady=10)
        self.settings_button = ctk.CTkButton(self, text="Einstellungen", command=lambda: switch_callback(EinstellungsPage))
        self.settings_button.pack(pady=10)
        self.singleplayer_button = ctk.CTkButton(self, text="Singleplayer")
        self.singleplayer_button.pack(pady=10)

class AnleitungsPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Anleitung")
        self.label2.pack(pady=20)
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.back_button.pack(pady=10)

class BestenlistPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Bestenliste")
        self.label2.pack(pady=20)
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.back_button.pack(pady=10)

class EinstellungsPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Einstellungen")
        self.label2.pack(pady=20)
        self.button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.button.pack(pady=10)

class SpielernamenPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Spielernamen eingeben")
        self.label2.pack(pady=20)
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.back_button.pack(pady=10)
        self.forward_button = ctk.CTkButton(self, text="weiter", command=lambda: switch_callback(HindernissPage))
        self.forward_button.pack(pady=10)

class HindernissPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Hindernissplan")
        self.label2.pack(pady=20)
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(SpielernamenPage))
        self.back_button.pack(pady=10)
        self.startgame_button = ctk.CTkButton(self, text="Spiel starten", command=lambda: switch_callback(SpielPage))
        self.startgame_button.pack(pady=10)

class SpielPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Spielpage")
        self.label2.pack(pady=20)
        self.closeround_button = ctk.CTkButton(self, text="Ich schliesse Runde X von 3 ab", command=lambda: switch_callback(ResultatPage))
        self.closeround_button.pack(pady=10)
        self.endgame_button = ctk.CTkButton(self, text="Spiel abbrechen", command=lambda: switch_callback(MainPage))
        self.endgame_button.pack(pady=10)
        self.explain_button = ctk.CTkButton(self, text="Anleitung", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10)

class ResultatPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Resultate")
        self.label2.pack(pady=20)
        self.again_button = ctk.CTkButton(self, text="Nochmals", command=lambda: switch_callback(HindernissPage))
        self.again_button.pack(pady=10)
        self.stop_button = ctk.CTkButton(self, text="Beenden", command=lambda: switch_callback(MainPage))
        self.stop_button.pack(pady=10)
        self.leaderboard_button = ctk.CTkButton(self, text="Bestenliste", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10)