import customtkinter as ctk

global inGame
inGame = False

class MainPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent

        # Labels
        self.label = ctk.CTkLabel(self, text="Mainpage")
        self.label.pack(padx=20, pady=20)

        # Selection
        self.playercount_var = ctk.StringVar()
        self.plyercount_button = ctk.CTkSegmentedButton(self, values=["Einzelspieler", "2 Spieler", "3 Spieler", "4 Spieler"],
                                                     command=self.getPlayercount,
                                                     variable=self.playercount_var)
        
        self.plyercount_button.pack()

        # Buttons
        self.explain_button = ctk.CTkButton(self, text="Anleitung", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10)
        self.leaderboard_button = ctk.CTkButton(self, text="Bestenliste", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10)
        self.start_button = ctk.CTkButton(self, text="Start", command=lambda: switch_callback(SpielernamenPage))
        self.start_button.pack(pady=10)
        self.settings_button = ctk.CTkButton(self, text="Einstellungen", command=lambda: switch_callback(EinstellungsPage))
        self.settings_button.pack(pady=10)

    def getPlayercount(self, value):
        print("segmented button clicked:", value)

class AnleitungsPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Anleitung")
        self.label2.pack(pady=20)

        # Buttons
        self.checkStatus(switch_callback)

    def checkStatus(self, switch_callback):
        if inGame:
            self.back_button = ctk.CTkButton(self, text="zurück zum Spiel", command=lambda: switch_callback(SpielPage))
            self.back_button.pack(pady=10)
        else: 
            self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
            self.back_button.pack(pady=10)

class BestenlistPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Bestenliste")
        self.label2.pack(pady=20)

        # Buttons
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.back_button.pack(pady=10)

        # Leaderboard
        self.createLeaderboard()
        

    def createLeaderboard(self):
        self.winner_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="1. ")
        self.winner_label.pack(pady=10)
        self.second_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="2.")
        self.second_label.pack(pady=10)
        self.third_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="3.")
        self.third_label.pack(pady=10)
        self.fourth_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="4.")
        self.fourth_label.pack(pady=10)
        self.fifth_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="5.")
        self.fifth_label.pack(pady=10)
        self.sixth_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="6.")
        self.sixth_label.pack(pady=10)
        self.seventh_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="7.")
        self.seventh_label.pack(pady=10)
        self.eighthwinner_label = ctk.CTkLabel(self, width=800, height=50, corner_radius=3, bg_color="blue", fg_color="blue", text_color="yellow", text="8.")
        self.eighthwinner_label.pack(pady=10)

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
        
        # Labels
        self.title = ctk.CTkLabel(self, text="Spielernamen eingeben")
        self.title.pack(pady=20)

        # Inputs
        self.playername_1_input = ctk.CTkEntry(self, placeholder_text="Spielername 1")
        self.playername_1_input.pack(pady=5)
        self.playername_2_input = ctk.CTkEntry(self, placeholder_text="Spielername 2")
        self.playername_2_input.pack(pady=5)
        self.playername_3_input = ctk.CTkEntry(self, placeholder_text="Spielername 3")
        self.playername_3_input.pack(pady=5)
        self.playername_4_input = ctk.CTkEntry(self, placeholder_text="Spielername 4")
        self.playername_4_input.pack(pady=5)

        # Buttons
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.back_button.pack(pady=10)
        self.forward_button = ctk.CTkButton(self, text="weiter", command=lambda: [switch_callback(HindernissPage), self.getSpielernamen()])
        self.forward_button.pack(pady=10)

    def getSpielernamen(self):
        self.playername_1 = self.playername_1_input.get()
        print(self.playername_1)
        self.playername_2 = self.playername_2_input.get()
        print(self.playername_2)
        self.playername_3 = self.playername_3_input.get()
        print(self.playername_3)
        self.playername_4 = self.playername_4_input.get()
        print(self.playername_4)
        

class HindernissPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Hindernissplan")
        self.label2.pack(pady=20)

        # Buttons
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(SpielernamenPage))
        self.back_button.pack(pady=10)
        self.startgame_button = ctk.CTkButton(self, text="Spiel starten", command=lambda: [switch_callback(SpielPage), self.updateStatus()])
        self.startgame_button.pack(pady=10)
        self.info_button = ctk.CTkButton(self, text="Info", command=lambda: switch_callback(InfoPage))
        self.info_button.pack(pady=10)
    
    def updateStatus(self):
        global inGame
        inGame = True

class SpielPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Spielpage")
        self.label2.pack(pady=20)

        # Buttons
        self.closeround_button = ctk.CTkButton(self, text="Ich schliesse Runde X von 3 ab", command=lambda: switch_callback(ResultatPage))
        self.closeround_button.pack(pady=10)
        self.endgame_button = ctk.CTkButton(self, text="Spiel abbrechen", command=lambda: [switch_callback(MainPage), self.updateStatus()])
        self.endgame_button.pack(pady=10)
        self.explain_button = ctk.CTkButton(self, text="Anleitung", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10)

    def updateStatus(self):
        global inGame
        inGame = False

class ResultatPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Gratulation!")
        self.label2.pack(pady=20)
        self.winner_label = ctk.CTkLabel(self, text="Gewinner")
        self.winner_label.pack(pady=20)
        self.second_label = ctk.CTkLabel(self, text="Zweiter")
        self.second_label.pack(pady=20)
        self.third_label = ctk.CTkLabel(self, text="Dritter")
        self.third_label.pack(pady=20)

        # Buttons
        self.again_button = ctk.CTkButton(self, text="Nochmals", command=lambda: switch_callback(HindernissPage))
        self.again_button.pack(pady=10)
        self.stop_button = ctk.CTkButton(self, text="Beenden", command=lambda: switch_callback(MainPage))
        self.stop_button.pack(pady=10)
        self.leaderboard_button = ctk.CTkButton(self, text="Bestenliste", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10)

class InfoPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Info")
        self.label2.pack(pady=20)

        # Buttons
        self.again_button = ctk.CTkButton(self, text="OK", command=lambda: switch_callback(HindernissPage))
        self.again_button.pack(pady=10)