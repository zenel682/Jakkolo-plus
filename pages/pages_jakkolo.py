import customtkinter as ctk

class MainPage(ctk.CTkFrame):
    global inGame
    inGame = False
    global score_player_1, score_player_2, score_player_3, score_player_4, score
    score_player_1 = 0
    score_player_2 = 0
    score_player_3 = 0
    score_player_4 = 0
    score = 0

    global name_player_1, name_player_2, name_player_3, name_player_4
    name_player_1 = ""
    name_player_2 = "" 
    name_player_3 = "" 
    name_player_4 = ""

    global round_number
    round_number = 1

    global puck_count
    puck_count = 30

    global rank_player_1, rank_player_2, rank_player_3, rank_player_4

    global count_ones, count_twos, count_threes, count_fours
    count_ones = 0
    count_twos = 0
    count_threes = 0
    count_fours = 0

    global player_count
    player_count = 1

    global current_player
    current_player = 1

    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        player_count = 1
        print("Playercount " + str(player_count))

        # Labels
        self.label = ctk.CTkLabel(self, text="Mainpage")
        self.label.pack(padx=20, pady=20)

        # Selection
        player_count = ctk.StringVar(value="Einzelspieler")
        self.playercount_button = ctk.CTkSegmentedButton(self, values=["Einzelspieler", "2 Spieler", "3 Spieler", "4 Spieler"],
                                                     command= self.getPlayercountAndDisableStart,
                                                     variable=player_count)
        
        self.playercount_button.pack()

        # Buttons
        self.explain_button = ctk.CTkButton(self, text="Anleitung", font=("Minion Pro Med", 20), command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10)
        self.leaderboard_button = ctk.CTkButton(self, text="Bestenliste", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10)
        self.start_button = ctk.CTkButton(self, text="Start", command=lambda: switch_callback(SpielernamenPage))
        self.start_button.pack(pady=10)
        self.settings_button = ctk.CTkButton(self, text="Einstellungen", command=lambda: switch_callback(EinstellungsPage))
        self.settings_button.pack(pady=10)
        self.start_button.configure(state="disabled")
        self.disableStart()

    def getPlayercount(self, value):
        global player_count
        if value == "Einzelspieler":
            player_count = 1
        elif value == "2 Spieler":
            player_count = 2
        elif value == "3 Spieler":
            player_count = 3
        elif value == "4 Spieler":
            player_count = 4
        else:
            player_count = 0

        print("segmented button clicked:", player_count)

    def disableStart(self):
        if player_count != 0:
            self.start_button.configure(state="normal")

        print("Im here")

    def getPlayercountAndDisableStart(self, value):
        self.getPlayercount(value)
        self.disableStart()

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
        self.disableInputs()

        # Buttons
        self.back_button = ctk.CTkButton(self, text="zurück", command=lambda: [switch_callback(MainPage), self.clearPlayercount()])
        self.back_button.pack(pady=10)
        self.forward_button = ctk.CTkButton(self, text="weiter", command=lambda: [switch_callback(HindernissPage), self.getSpielernamen()])
        self.forward_button.pack(pady=10)

    def getSpielernamen(self):
        if self.playername_1_input.get() != "":
            name_player_1 = self.playername_1_input.get()
        else:
            name_player_1 = "Standardspieler 1"

        if self.playername_2_input.get() != "":
            name_player_2 = self.playername_2_input.get()
        else:
            name_player_2 = "Standardspieler 2"

        if self.playername_3_input.get() != "":
            name_player_3 = self.playername_3_input.get()
        else:
            name_player_3 = "Standardspieler 3"

        if self.playername_4_input.get() != "":
            name_player_4 = self.playername_4_input.get()
        else:
            name_player_4 = "Standardspieler 4"

        global current_player
        current_player = name_player_1

        print(name_player_1)
        print(name_player_2)
        print(name_player_3)      
        print(name_player_4)
 

    def disableInputs(self):
        if player_count == 1:
            self.playername_2_input.configure(state="disabled")
            self.playername_3_input.configure(state="disabled")
            self.playername_4_input.configure(state="disabled")
        elif player_count == 2:
            self.playername_3_input.configure(state="disabled")
            self.playername_4_input.configure(state="disabled")
        elif player_count == 3:
            self.playername_4_input.configure(state="disabled")

    def clearPlayercount(self):
        global player_count
        player_count = 1
        

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
        self.points_label = ctk.CTkLabel(self, text=f"Punkte: {score}")
        self.points_label.pack(pady=20)
        self.currentplayer_label = ctk.CTkLabel(self, text=current_player)
        self.currentplayer_label.pack(pady=20)
        self.round_label = ctk.CTkLabel(self, text=f"Runde {round_number}/3")
        self.round_label.pack(pady=20)

        # Buttons
        self.showContinueOrFinishButton(switch_callback)
        #self.closeround_button = ctk.CTkButton(self, text="Ich schliesse Runde X von 3 ab", command=lambda: [switch_callback(RundenPage), self.increaseRoundnumber()])
        #self.closeround_button.pack(pady=10)
        self.endgame_button = ctk.CTkButton(self, text="Spiel abbrechen", command=lambda: [switch_callback(MainPage), self.updateStatus()])
        self.endgame_button.pack(pady=10)
        self.explain_button = ctk.CTkButton(self, text="Anleitung", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10)

    def updateStatus(self):
        global inGame
        inGame = False
        global round_number
        round_number = 1

    def increaseRoundnumber(self):
        global round_number
        if round_number < 3:
            round_number += 1
        else:
            round_number = 1

    def showContinueOrFinishButton(self, switch_callback):
        global round_number
        if round_number < 3:
            self.closeround_button = ctk.CTkButton(self, text=f"Ich schliesse Runde {round_number} von 3 ab", command=lambda: [switch_callback(RundenPage), self.increaseRoundnumber()])
            self.closeround_button.pack(pady=10)
        else: 
            self.endplayerturn_button = ctk.CTkButton(self, text="Ich beende meine Spielzüge", command=lambda: [switch_callback(ResultatPage), self.updateStatus()])
            self.endplayerturn_button.pack(pady=10)


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

class RundenPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Zwischen Runden Page")
        self.label2.pack(pady=20)

        # Buttons
        self.again_button = ctk.CTkButton(self, text="Pucks eingesammelt", command=lambda: switch_callback(SpielPage))
        self.again_button.pack(pady=10)