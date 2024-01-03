"""
This file contains all information about the pages of the Jakkolo plus GUI
"""

# Imports
import customtkinter as ctk
from leaderboard_jakkolo import Leaderboard
import threading 
from keyboard_class import KeyCounter
from PIL import Image, ImageTk

# Status and game status information
global inGame
inGame = False
global lastpage
lastpage = "MainPage"
global old_player_name
old_player_name = ""
global round_number
round_number = 1
global players_played_counter
players_played_counter = 0
global puck_count
puck_count = 30

# Player informations
global name_player_1, name_player_2, name_player_3, name_player_4, names
name_player_1 = ""
name_player_2 = "" 
name_player_3 = "" 
name_player_4 = ""
global current_player_name
current_player_name = ""
global player_count
player_count = 1


# Score information
global score_player_1, score_player_2, score_player_3, score_player_4, score, scores
score_player_1 = 0
score_player_2 = 0
score_player_3 = 0
score_player_4 = 0
score = 0
scores = []
global count_ones, count_twos, count_threes, count_fours
count_ones = 0
count_twos = 0
count_threes = 0
count_fours = 0
global rank_player_1, rank_player_2, rank_player_3, rank_player_4

# Leaderboard
global lb_current
lb_current = []
global list_current_players_scores
list_current_players_scores = []

# Endschalter and Keycounter
global keycounter

class MainPage(ctk.CTkFrame):
    global lb_pnames_pscores
    lb = Leaderboard()
    lb_pnames_pscores = lb.openAndReadJSON()

    def __init__(self, parent, switch_callback, width, height, fg_color):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent

        #Thread
        self.thread1 = None   
        self.stop_flag = threading.Event()

        # Endschalter and Keycounter
        global keycounter
        keycounter = KeyCounter(stop_flag=self.stop_flag)
        
        # Status information
        global lastpage
        lastpage = "MainPage"
        player_count = 1

        # Fonts
        global big_font_mp
        big_font_mp = ctk.CTkFont(family="Minion Pro Med",
                           size=46,
                           weight="bold")    
        global medium_font_mp
        medium_font_mp = ctk.CTkFont(family="Minion Pro Med",
                           size=30,
                           weight="bold")  
        global small_font_mp
        small_font_mp = ctk.CTkFont(family="Minion Pro Med",
                           size=20,
                           weight="normal")  
     
        # Labels
        self.label = ctk.CTkLabel(self, text="Jakkolo Plus", font=big_font_mp, text_color="#547AA5")
        self.label.place(x=512, y=40, anchor='center')

        # Selection
        player_count = ctk.StringVar(value="Einzelspieler")
        self.playercount_button = ctk.CTkSegmentedButton(master=self, height=90, width=500,dynamic_resizing=False, values=["Einzelspieler", "2 Spieler", "3 Spieler", "4 Spieler"],
                                                         font=small_font_mp, text_color="#FFFFFF", command= self.getPlayercountAndDisableStart, selected_color="#547AA5", fg_color="#474044", unselected_color="#D9D9D9", unselected_hover_color="#828282", selected_hover_color="#324963", corner_radius=15,
                                                         variable=player_count)
        
        self.playercount_button.place(x=512, y=125, anchor='center')
        # Buttons
        #self.settings_button = ctk.CTkButton(self, text="", image=ctk.CTkImage(light_image=Image.open("icons\settings_icon.png"), dark_image=Image.open("icons\settings_icon.png"), size=(30,30)), command=lambda: switch_callback(EinstellungsPage))
        #self.settings_button.pack(padx=100, pady=30, side=ctk.RIGHT)
        self.quit_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Quit", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [self.on_close(), self.stop_tracker()])
        self.quit_button.place(x=512, y=530, anchor='center')
        self.leaderboard_button = ctk.CTkButton(master=self, width=500, height=90, corner_radius=25, text="Bestenliste", text_color="#FFFFFF", font=big_font_mp, fg_color="#4F5165", hover_color="#2F303C", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.place(x=512, y=430, anchor='center')
        self.explain_button = ctk.CTkButton(master=self, width=500, height=90, corner_radius=25, text="Anleitung", text_color="#FFFFFF", font=big_font_mp, fg_color="#50D8D7", hover_color="#209190", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.place(x=512, y=330, anchor='center')
        self.start_button = ctk.CTkButton(master=self, width=500, height=90, corner_radius=25, text="Start", text_color="#FFFFFF", font=big_font_mp, fg_color="#50D8D7", hover_color="#209190", command=lambda: [switch_callback(SpielernamenPage), self.start_tracker()])
        self.start_button.place(x=512, y=230, anchor='center')

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

    def disableStart(self):
        if player_count != 0:
            self.start_button.configure(state="normal")

    def getPlayercountAndDisableStart(self, value):
        self.getPlayercount(value)
        self.disableStart()

    def start_tracker(self):
        print("Start Tracking")
        # Toggle on Raspi or PC
        #self.display_var = endschalter.b1_counter
        #endschalter.read_it = True  
        try:
            self.start = True
            print("Thread started")
        except Exception as e:
            print(f"Error starting thread: {e}")
            self.thread1 = None  # Set thread1 to None if an exception occurs

    def run_keycounter(self):    
        self.keycounter.run(stop_flag=self.stop_flag)  # Pass the stop_flag to the run method
    
    def stop_tracker(self):
        if self.thread1 and self.thread1.is_alive():
            self.stop_flag.set()
            #self.keycounter.stop()
            self.thread1.join(timeout=3)
            print("Joined threads")
        else:
            print("Thread was not opened yet")

    def on_close(self):
        print("Close app")
        self.stop_tracker()
        self.lb.safeAndCloseJSON(lb_pnames_pscores)
        self.parent.destroy()

class AnleitungsPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        # Labels
        self.anleitungs_label = ctk.CTkLabel(self, text="Anleitung", font=big_font_mp, text_color="#547AA5")
        self.anleitungs_label.place(x=512, y=40, anchor='center')

        # Buttons
        self.checkStatus(switch_callback)

    def checkStatus(self, switch_callback):
        global inGame
        if inGame:
            self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück zum Spiel", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(SpielPage))
            self.back_button.place(x=512, y=400, anchor='center')
        else: 
            self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(MainPage))
            self.back_button.place(x=512, y=400, anchor='center')

class BestenlistPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent

        # Labels
        self.bestenlisten_label = ctk.CTkLabel(self, text="Bestenliste", font=big_font_mp, text_color="#547AA5")
        self.bestenlisten_label.place(x=512, y=40, anchor='center')

        # Leaderboard
        self.createLeaderboard()

        # Buttons
        self.checkStatus(switch_callback)

    def createLeaderboard(self):  
        for i in range(10):
            if i % 2:
                colorpattern = "#547AA5"
            else:
                colorpattern = "#4F5165"

            self.rank_label = ctk.CTkLabel(self, width=50, height=35, corner_radius=5, anchor=ctk.CENTER, fg_color=colorpattern, text_color="#FFFFFF", font=small_font_mp, text=f"{i+1}.")
            self.name_label = ctk.CTkLabel(self, width=350, height=35, corner_radius=5, anchor=ctk.W, fg_color=colorpattern, text_color="#FFFFFF", font=small_font_mp, text=lb_pnames_pscores[i][0])
            self.score_label = ctk.CTkLabel(self, width=125, height=35, corner_radius=5, anchor=ctk.E, fg_color=colorpattern, text_color="#FFFFFF", font=small_font_mp, text=lb_pnames_pscores[i][1])
            
            self.rank_label.place(x=277, y=100+i*42, anchor='center')
            self.name_label.place(x=485, y=100+i*42, anchor='center')
            self.score_label.place(x=730, y=100+i*42, anchor='center')

    def checkStatus(self, switch_callback):
        global lastpage
        if lastpage == "ResultatPage":
            self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(ResultatPage))
            self.back_button.place(x=512, y=550, anchor='center')
        else: 
            self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(MainPage))
            self.back_button.place(x=512, y=550, anchor='center')

class EinstellungsPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        self.einstellungen_label = ctk.CTkLabel(self, text="Einstellungen", font=big_font_mp, text_color="#547AA5")
        self.einstellungen_label.place(x=512, y=40, anchor='center')
        self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(MainPage))
        self.back_button.place(x=512, y=400, anchor='center')

class SpielernamenPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent

        # Fonts
        global alphabet_font
        alphabet_font = ctk.CTkFont(family="Minion Pro Med",
                           size=25,
                           weight="normal") 
        global playername_font
        playername_font = ctk.CTkFont(family="Minion Pro Med",
                           size=30,
                           weight="bold") 
        
        # Labels
        #self.title = ctk.CTkLabel(self, text="Spielernamen eingeben", font=big_font_mp, text_color="#547AA5")
        #self.title.place(x=512, y=35, anchor='center')

        # Inputs
        self.playername_1_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 1")
        self.playername_1_input.place(x=512, y=160, anchor='center')
        self.playername_2_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 2")
        self.playername_2_input.place(x=512, y=230, anchor='center')
        self.playername_3_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 3")
        self.playername_3_input.place(x=512, y=300, anchor='center')
        self.playername_4_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 4")
        self.playername_4_input.place(x=512, y=370, anchor='center')
        self.disableInputs()


        # Option two with colors
        letterheight = 20
        letterwidth = 20
        letterradius = 3
        #self.title = ctk.CTkLabel(self, text="Farbe aussuchen", font=big_font_mp, text_color="#547AA5")
        #self.title.place(x=512, y=35, anchor='center')
        self.player1_label = ctk.CTkLabel(self, text="Spieler 1", font=medium_font_mp, text_color="#547AA5")
        #self.player1_label.place(x=100, y=150, anchor='center')
        self.color_1_player_1 = ctk.CTkButton(self, width=80, height=80, corner_radius=15, fg_color="pink", hover_color="red", text="")
        #self.color_1_player_1.place(x=512, y=150, anchor='center')

        # Alphabet buttons
        self.A_button = ctk.CTkButton(self, width=letterwidth, height=letterheight, font=alphabet_font, corner_radius=letterradius, fg_color="blue", text="A",  text_color="#547AA5", command=lambda: self.write_letter("A"))
        self.A_button.place(x=100, y=100, anchor='center')
        self.B_button = ctk.CTkButton(self, width=letterwidth, height=letterheight, font=alphabet_font, corner_radius=letterradius, fg_color="blue", text="B",  text_color="#547AA5", command=lambda: self.write_letter("B"))
        self.B_button.place(x=130, y=100, anchor='center')
        self.C_button = ctk.CTkButton(self, width=letterwidth, height=letterheight, font=alphabet_font, corner_radius=letterradius, fg_color="blue", text="C",  text_color="#547AA5", command=lambda: self.write_letter("C"))
        self.C_button.place(x=160, y=100, anchor='center')
        self.DEL_button = ctk.CTkButton(self, width=letterwidth, height=letterheight, font=alphabet_font, corner_radius=letterradius, fg_color="blue", text="DEL",  text_color="#547AA5", command=lambda: self.delete_letter())
        self.DEL_button.place(x=240, y=100, anchor='center')
        self.ENTER_button = ctk.CTkButton(self, width=letterwidth, height=letterheight, font=alphabet_font, corner_radius=letterradius, fg_color="blue", text="ENTER",  text_color="#547AA5", command=lambda: self.enter())
        self.ENTER_button.place(x=350, y=100, anchor='center')

        self.name_array = []
        self.name = ""

        self.name_1 = ""
        self.name_2 = ""
        self.name_3 = ""
        self.name_4 = ""    

        self.name_1_label = ctk.CTkLabel(master=self, text=self.name, font=playername_font)
        self.name_1_label.place(x=200, y=200)
        self.name_2_label = ctk.CTkLabel(master=self, text=self.name, font=playername_font)
        self.name_2_label.place(x=200, y=250)
        self.name_3_label = ctk.CTkLabel(master=self, text=self.name, font=playername_font)
        self.name_3_label.place(x=200, y=300)
        self.name_4_label = ctk.CTkLabel(master=self, text=self.name, font=playername_font)
        self.name_4_label.place(x=200, y=350)

        self.current_name_label = self.name_1_label

        # Buttons
        self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(MainPage), self.clearPlayercount(), self.clearLeaderboard()])
        self.back_button.place(x=45, y=510)
        self.forward_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="weiter", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(HindernissPage), self.getSpielernamen2(), self.createListOfCurrentPlayers()])
        self.forward_button.place(x=840, y=510)

        self.after(250, self.updateNameLabel)

    def write_letter(self, letter):
        self.name_array.append(letter)
        print(letter)

    def delete_letter(self):
        if len(self.name_array) != 0:
            self.name_array.pop()
            print("delete")

    def enter(self):
        if self.current_name_label == self.name_1_label:
            if player_count == 1:
                print("nothing cuase 1 player")
                self.name_1 = list(self.name_array)
            elif player_count >= 2:
                print("change label to 2")
                self.name_1 = list(self.name_array)
                self.name_array = list(self.name_2)
                self.current_name_label = self.name_2_label
        elif self.current_name_label == self.name_2_label:
            if player_count == 2:
                print("change back to 1")
                self.name_2 = list(self.name_array)
                self.name_array = list(self.name_1)
                self.current_name_label = self.name_1_label
            elif player_count >= 3:
                print("change label to 3")
                self.name_2 = list(self.name_array)
                self.name_array = list(self.name_3)   
                self.current_name_label = self.name_3_label
        elif self.current_name_label == self.name_3_label:
            if player_count == 3:
                print("change back to 1")
                self.name_3 = list(self.name_array)
                self.name_array = list(self.name_1)
                self.current_name_label = self.name_1_label
            elif player_count >= 4:
                print("change label to 4")
                self.name_3 = list(self.name_array)
                self.name_array = list(self.name_4)
                self.current_name_label = self.name_4_label
        elif self.current_name_label == self.name_4_label:
            if player_count == 4:
                print("change back to 1")
                self.name_4 = list(self.name_array)
                self.name_array = list(self.name_1)
                self.current_name_label = self.name_1_label
            else:
                print("Error")
        else:
            print("Error2")

        print("Enter")
    
    def updateNameLabel(self):
        self.name = self.removeSpaces(self.listToString(self.name_array))
        self.current_name_label.configure(text=self.name)
        self.after(250, self.updateNameLabel)    

    # Function to convert
    def listToString(self, list):
        # initialize an empty string
        str1 = " "
        # return string
        return (str1.join(list))

    def getSpielernamen2(self):
        global name_player_1, name_player_2, name_player_3, name_player_4
        if self.name_1 != []:
            name_player_1 = self.removeSpaces(self.listToString(self.name_1))
        else:
            name_player_1 = "Standardspieler 1"

        if self.name_2 != []:
            name_player_2 = self.removeSpaces(self.listToString(self.name_2))
        else:
            name_player_2 = "Standardspieler 2"

        if self.name_3 != []:
            name_player_3 = self.removeSpaces(self.listToString(self.name_3))
        else:
            name_player_3 = "Standardspieler 3"

        if self.name_4!= []:
            name_player_4 = self.removeSpaces(self.listToString(self.name_4))
        else:
            name_player_4 = "Standardspieler 4"

        global current_player
        current_player = name_player_1

        print(name_player_1)
        print(name_player_2)
        print(name_player_3)      
        print(name_player_4)

    def removeSpaces(self, string):
        return string.replace(" ", "")

    def getSpielernamen(self):
        global name_player_1, name_player_2, name_player_3, name_player_4
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

    def createListOfCurrentPlayers(self):
        global name_player_1, name_player_2, name_player_3, name_player_4
        global list_current_players_scores
        if player_count >= 1:
            list_current_players_scores.append((name_player_1, score_player_1))
        if player_count >= 2:
            list_current_players_scores.append((name_player_2, score_player_2))
        if player_count >= 3:
            list_current_players_scores.append((name_player_3, score_player_3))
        if player_count == 4:
            list_current_players_scores.append((name_player_4, score_player_4))
        print("List of current players and scores: " + str(list_current_players_scores))

    def clearLeaderboard(self):
        global list_current_players_scores
        list_current_players_scores.clear()

class HindernissPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Hindernissplan", font=big_font_mp, text_color="#547AA5")
        self.label2.place(x=512, y=40, anchor='center')

        # Buttons
        self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(SpielernamenPage))
        self.back_button.place(x=45, y=510)
        self.startgame_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Spiel starten", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(SpielPage), self.updateStatus()])
        self.startgame_button.place(x=820, y=510)
        self.info_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Info", text_color="#000000", font=small_font_mp, fg_color="#FF5757", hover_color="#CD0000", command=lambda: switch_callback(InfoPage))
        self.info_button.place(x=512, y=510, anchor='n')
    
    def updateStatus(self):
        global inGame
        inGame = True
        keycounter.var1 = 0
        keycounter.var2 = 0
        keycounter.var3 = 0
        keycounter.var4 = 0

class SpielPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent

        global count_ones, count_twos, count_threes, count_fours
        global puck_count
        global list_current_players_scores
        global players_played_counter
        global current_player_name, old_player_name
        current_player_name = list_current_players_scores[players_played_counter][0]

        # Labels
        self.points_label = ctk.CTkLabel(self, text=f"Punkte: {score}", font=medium_font_mp, text_color="#000000")
        self.points_label.place(x=460, y=50)
        self.currentplayer_label = ctk.CTkLabel(self, text=current_player_name, font=medium_font_mp, text_color="#000000")
        self.currentplayer_label.place(x=60, y=50)
        self.round_label = ctk.CTkLabel(self, text=f"Runde {round_number}/3", font=small_font_mp, text_color="#000000")
        self.round_label.place(x=60, y=90)

        # Create image
        self.goal_image_org = Image.open("icons\jakkolo_goal.png")
        self.resized_goal_image = self.goal_image_org.resize((1480, 448))
        self.goal_image = ImageTk.PhotoImage(self.resized_goal_image)
        self.canvas = ctk.CTkCanvas(self, width=1480, height=448, background="#474044", highlightthickness=0)
        self.canvas.place(x=150, y=350)
        self.canvas.create_image(740, 224, anchor=ctk.CENTER, image=self.goal_image)

        # Labels for pucks in each target
        self.count_ones_label = ctk.CTkLabel(self.canvas, text=count_ones, font=big_font_mp)
        self.count_ones_label.place(x=113, y=160, anchor='center')
        self.count_twos_label = ctk.CTkLabel(self.canvas, text=count_twos, font=big_font_mp)
        self.count_twos_label.place(x=283, y=160, anchor='center')
        self.count_threes_label = ctk.CTkLabel(self.canvas, text=count_threes, font=big_font_mp)
        self.count_threes_label.place(x=456, y=160, anchor='center')
        self.count_fours_label = ctk.CTkLabel(self.canvas, text=count_fours, font=big_font_mp)
        self.count_fours_label.place(x=629, y=160, anchor='center')

        # Label for puck count
        #self.puck_count_label = ctk.CTkLabel(self, text=f"Verbleibende Pucks: {puck_count}")
        #self.puck_count_label.place(x=600, y=90)

        # Buttons
        self.showContinueOrFinishButton(switch_callback)
        self.explain_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Anleitung", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.place(x=510, y=510)
        self.endgame_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Spiel abbrechen", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(MainPage), self.updateStatus(), self.clearLeaderboard()])
        self.endgame_button.place(x=776, y=510)

        self.resetScoreNewPlayer()
        old_player_name = current_player_name
        self.after(250, self.update_variable)

    def resetScoreNewPlayer(self):
        global current_player_name, old_player_name, score
        global count_ones, count_twos, count_threes, count_fours
        if current_player_name != old_player_name:
            print("okke")
            keycounter.var1 = 0
            keycounter.var2 = 0
            keycounter.var3 = 0
            keycounter.var4 = 0
            count_ones = 0
            count_twos = 0
            count_threes = 0
            count_fours = 0
            score = 0

    def update_variable(self):
        global count_ones, count_twos, count_threes, count_fours, score, scores
        count_ones = keycounter.var1
        count_twos = keycounter.var2
        count_threes = keycounter.var3
        count_fours = keycounter.var4
        self.calculateScore()
        self.count_ones_label.configure(text=count_ones)
        self.count_twos_label.configure(text=count_twos)
        self.count_threes_label.configure(text=count_threes)
        self.count_fours_label.configure(text=count_fours)
        self.points_label.configure(text=f"Punkte: {score}")
        self.after(250, self.update_variable)

    def updateStatus(self):
        global inGame, score
        inGame = False
        global round_number
        round_number = 1

    def resetRoundnumber(self):
        global round_number, score, count_ones, count_twos, count_threes, count_fours
        round_number = 1

    def clearLeaderboard(self):
        global list_current_players_scores
        list_current_players_scores.clear()

    def increaseRoundnumber(self):
        global round_number, score, count_ones, count_twos, count_threes, count_fours
        if round_number == 3:
            keycounter.var1 = 0
            keycounter.var2 = 0
            keycounter.var3 = 0
            keycounter.var4 = 0
            count_ones = 0
            count_twos = 0
            count_threes = 0
            count_fours = 0
        if round_number < 3:
            round_number += 1
        else:
            round_number = 1
            count_ones = 0
            count_twos = 0
            count_threes = 0
            count_fours = 0

    def showContinueOrFinishButton(self, switch_callback):
        global round_number, score, count_ones, count_twos, count_threes, count_fours
        if round_number < 3:
            self.closeround_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text=f"Ich schliesse Runde {round_number} von 3 ab", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(RundenPage), self.increaseRoundnumber()])
            self.closeround_button.place(x=55, y=510)
        else:      
            count_ones = 0
            count_twos = 0
            count_threes = 0
            count_fours = 0
            self.checkIfThereAreMorePlayers(switch_callback)
            self.resetRoundnumber()

    def createCurrentLeaderboard(self):
        global list_current_players_scores     
        global lb_pnames_pscores
        global players_played_counter
        self.updateScore()
        print(list_current_players_scores)
        print(lb_pnames_pscores)
        for i in range(len(list_current_players_scores)):
            for j in range(len(lb_pnames_pscores)):
                if list_current_players_scores[i][1] > lb_pnames_pscores[j][1]:
                    lb_pnames_pscores.insert(j, list_current_players_scores[i])
                    break
        players_played_counter = 0

    def checkIfThereAreMorePlayers(self, switch_callback):
        global players_played_counter, score
        if players_played_counter < player_count-1:
            self.endplayerturn_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25,text="Nächster Spieler ist dran", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(RundenPage), self.resetRoundnumber(), self.updateScore()])
            self.endplayerturn_button.place(x=55, y=510)
        else:      
            self.endplayerturn_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25,text="Spiel ganz abschliessen", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [self.createCurrentLeaderboard(), switch_callback(ResultatPage), self.updateStatus(), self.resetRoundnumber()])
            self.endplayerturn_button.place(x=55, y=510)

    def updateScore(self):
        global score
        global players_played_counter, list_current_players_scores
        global count_ones, count_twos, count_threes, count_fours
        self.calculateScore()
        print(players_played_counter)
        list_current_players_scores[players_played_counter] = (current_player_name, score)
        players_played_counter += 1
        keycounter.var1 = 0
        keycounter.var2 = 0
        keycounter.var3 = 0
        keycounter.var4 = 0
        count_ones = 0
        count_twos = 0
        count_threes = 0
        count_fours = 0
        score = 0             

    def calculateScore(self):
        global scores, score, count_ones, count_twos, count_threes, count_fours
        scores = [count_ones, count_twos, count_threes, count_fours]
        lowest_count = min(scores)
        score_ones = count_ones
        score_twos = count_twos * 2
        score_threes = count_threes * 3
        score_fours = count_fours * 4
        score = lowest_count * 10 + score_ones + score_twos + score_threes + score_fours      

class ResultatPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent

        # Status
        global list_current_players_scores
        global lb_pnames_pscores
        global inGame, lastpage
        lastpage = "ResultatPage"
        list_current_players_scores = self.arrangeCurrentLeaderboard(list_current_players_scores)

        if player_count == 1:
            # Labels
            self.winner_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#DAA520", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[0][0]} ist Sieger*in! \nmit {list_current_players_scores[0][1]} Punkten")
            self.winner_label.place(x=512, y=80, anchor='center')
        elif player_count == 2:
            # Labels
            self.winner_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#DAA520", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[0][0]} ist Sieger*in! \nmit {list_current_players_scores[0][1]} Punkten")
            self.winner_label.place(x=512, y=80, anchor='center')
            self.second_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#C0C0C0", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[1][0]} ist Zweite*r! \nmit {list_current_players_scores[1][1]} Punkten")
            self.second_label.place(x=270, y=200, anchor='center')
        elif player_count == 3:
            # Labels
            self.winner_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#DAA520", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[0][0]} ist Sieger*in! \nmit {list_current_players_scores[0][1]} Punkten")
            self.winner_label.place(x=512, y=80, anchor='center')
            self.second_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#CD7F32", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[1][0]} ist Zweite*r! \nmit {list_current_players_scores[1][1]} Punkten")
            self.second_label.place(x=270, y=200, anchor='center')
            self.third_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#C0C0C0", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[2][0]} ist Dritte*r! \nmit {list_current_players_scores[2][1]} Punkten")
            self.third_label.place(x=738, y=200, anchor='center')
        elif player_count == 4:
            # Labels
            self.winner_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#DAA520", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[0][0]} ist Sieger*in! \nmit {list_current_players_scores[0][1]} Punkten")
            self.winner_label.place(x=512, y=80, anchor='center')
            self.second_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#CD7F32", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[1][0]} ist Zweite*r! \nmit {list_current_players_scores[1][1]} Punkten")
            self.second_label.place(x=270, y=200, anchor='center')
            self.third_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#C0C0C0", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[2][0]} ist Dritte*r! \nmit {list_current_players_scores[2][1]} Punkten")
            self.third_label.place(x=738, y=200, anchor='center')
            self.fourth_label = ctk.CTkLabel(master=self, width=80, height=50, corner_radius=25, fg_color="#624A2E", text_color="#FFFFFF", font=medium_font_mp, text=f"{list_current_players_scores[3][0]} ist Vierte*r! \nmit {list_current_players_scores[3][1]} Punkten")
            self.fourth_label.place(x=512, y=300, anchor='center')
        else:
            print("error with playercount")

        # Buttons
        self.again_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Nochmals", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(HindernissPage))
        self.again_button.place(x=350, y=510)
        self.stop_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Beenden", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(MainPage), self.updateStatus()])
        self.stop_button.place(x=550, y=510)
        self.leaderboard_button = ctk.CTkButton(master=self, width=200, height=90, corner_radius=25, text="Bestenliste", text_color="#FFFFFF", font=medium_font_mp, fg_color="#4F5165", hover_color="#2F303C", command=lambda: [switch_callback(BestenlistPage), self.setInGameStatus()])
        self.leaderboard_button.place(x=512, y=420, anchor='center')

    def updateStatus(self):
        global list_current_players_scores
        list_current_players_scores.clear()

    def setInGameStatus(self):
        global inGame
        inGame = True

    def arrangeCurrentLeaderboard(self, list):
        reverse = True #(Sorts in Ascending order) 
        # key is set to sort using second element of 
        # sublist lambda has been used 
        return(sorted(list, key = lambda x: x[1], reverse=reverse))  
        
class InfoPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Info", font=big_font_mp, text_color="#547AA5")
        self.label2.place(x=512, y=40, anchor='center')

        # Buttons
        self.again_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="OK", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(HindernissPage))
        self.again_button.place(x=512, y=510, anchor='center')

class RundenPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        global count_ones, count_twos, count_threes, count_fours
        self.ones_during_pause = 0
        self.ones_before_pause = count_ones
        self.twos_during_pause = 0
        self.twos_before_pause = count_twos
        self.threes_during_pause = 0
        self.threes_before_pause = count_threes
        self.fours_during_pause = 0
        self.fours_before_pause = count_fours
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Zwischen Runden Page", font=big_font_mp, text_color="#547AA5")
        self.label2.place(x=512, y=40, anchor='center')

        # Buttons
        self.again_button = ctk.CTkButton(master=self, width=150, height=90, corner_radius=25, text="Pucks eingesammelt", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [self.recalculateCount(), switch_callback(SpielPage)])
        self.again_button.place(x=512, y=510, anchor='center')

    def recalculateCount(self):
        keycounter.var1 = self.ones_before_pause - self.ones_during_pause
        keycounter.var2 = self.twos_before_pause - self.threes_during_pause
        keycounter.var3 = self.threes_before_pause - self.threes_during_pause
        keycounter.var4 = self.fours_before_pause - self.fours_during_pause