import customtkinter as ctk
from leaderboard_jakkolo import Leaderboard
import threading 
from keyboard_class import KeyCounter
from PIL import Image, ImageTk

class MainPage(ctk.CTkFrame):
    global inGame
    inGame = False
    global score_player_1, score_player_2, score_player_3, score_player_4, score, scores
    score_player_1 = 0
    score_player_2 = 0
    score_player_3 = 0
    score_player_4 = 0
    score = 0
    scores = []

    global name_player_1, name_player_2, name_player_3, name_player_4, names
    name_player_1 = ""
    name_player_2 = "" 
    name_player_3 = "" 
    name_player_4 = ""

    global round_number
    round_number = 1
    global players_played_counter
    players_played_counter = 0

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

    global current_player_name

    global lb_pnames_pscores
    global lb_current
    lb_current = []
    global list_current_players_scores
    list_current_players_scores = []

    lb = Leaderboard()
    lb_pnames_pscores = lb.openAndReadJSON()

    global keycounter



    def __init__(self, parent, switch_callback, width, height, fg_color):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        player_count = 1


        self.stop_flag = threading.Event()
        global keycounter
        keycounter = KeyCounter(stop_flag=self.stop_flag)
        
        self.thread1 = None     
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
        
        
        print("Playercount " + str(player_count))
        print("currentlb: " + str(list_current_players_scores))
     
        # Labels
        self.label = ctk.CTkLabel(self, text="Jakkolo Plus", font=big_font_mp, text_color="#547AA5")
        self.label.pack(pady=10, anchor=ctk.N, side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # Selection
        player_count = ctk.StringVar(value="Einzelspieler")
        self.playercount_button = ctk.CTkSegmentedButton(master=self, height=96, width=500,dynamic_resizing=False, values=["Einzelspieler", "2 Spieler", "3 Spieler", "4 Spieler"],
                                                         font=small_font_mp, text_color="#FFFFFF", command= self.getPlayercountAndDisableStart, selected_color="#547AA5", fg_color="#474044", unselected_color="#D9D9D9", unselected_hover_color="#828282", selected_hover_color="#324963", corner_radius=15,
                                                         variable=player_count)
        
        self.playercount_button.pack(pady=10, side=ctk.TOP)
        # Buttons
        #self.settings_button = ctk.CTkButton(self, text="", image=ctk.CTkImage(light_image=Image.open("icons\settings_icon.png"), dark_image=Image.open("icons\settings_icon.png"), size=(30,30)), command=lambda: switch_callback(EinstellungsPage))
        #self.settings_button.pack(padx=100, pady=30, side=ctk.RIGHT)

        self.quit_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Quit", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [self.on_close(), self.stop_tracker()])
        self.quit_button.pack(pady=10, anchor=ctk.CENTER,side=ctk.BOTTOM)
        self.leaderboard_button = ctk.CTkButton(master=self, width=500, height=90, corner_radius=25, text="Bestenliste", text_color="#FFFFFF", font=big_font_mp, fg_color="#4F5165", hover_color="#2F303C", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10, anchor=ctk.CENTER,side=ctk.BOTTOM)
        self.explain_button = ctk.CTkButton(master=self, width=500, height=90, corner_radius=25, text="Anleitung", text_color="#FFFFFF", font=big_font_mp, fg_color="#50D8D7", hover_color="#209190", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.pack(pady=10, anchor=ctk.CENTER,side=ctk.BOTTOM)
        self.start_button = ctk.CTkButton(master=self, width=500, height=90, corner_radius=25, text="Start", text_color="#FFFFFF", font=big_font_mp, fg_color="#50D8D7", hover_color="#209190", command=lambda: [switch_callback(SpielernamenPage), self.start_tracker()])
        self.start_button.pack(pady=10, anchor=ctk.CENTER, side=ctk.BOTTOM)

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
        self.label2 = ctk.CTkLabel(self, text="Anleitung", font=big_font_mp, text_color="#FFFFFF")
        self.label2.pack(pady=20)

        # Buttons
        self.checkStatus(switch_callback)
        self.puck_count_label = ctk.CTkLabel(self, text=f"Verbleibende Pucks: {puck_count}")
        self.puck_count_label.place(x = 10, y = 10, anchor = 'center')

    def checkStatus(self, switch_callback):
        if inGame:
            self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück zum Spiel", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(SpielPage))
            self.back_button.pack(pady=5, anchor=ctk.CENTER,side=ctk.BOTTOM)
        else: 
            self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(MainPage))
            self.back_button.pack(pady=5, anchor=ctk.CENTER,side=ctk.BOTTOM)


class BestenlistPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Bestenliste", font=big_font_mp, text_color="#FFFFFF")
        self.label2.pack(pady=15)

        # Leaderboard
        self.createLeaderboard(fg_color=fg_color)

        # Buttons
        self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(MainPage))
        self.back_button.pack(pady=5, anchor=ctk.CENTER,side=ctk.BOTTOM)

    def createLeaderboard(self, fg_color):
            
        for i in range(10):
            # Create a frame for each row of three labels
            frame = ctk.CTkFrame(self, fg_color=fg_color)
            frame.pack(side=ctk.TOP)

            if i % 2:
                colorpattern = "#547AA5"
            else:
                colorpattern = "#4F5165"

            self.rank_label = ctk.CTkLabel(frame, width=50, height=35, corner_radius=5, anchor=ctk.CENTER, fg_color=colorpattern, text_color="#FFFFFF", font=small_font_mp, text=f"{i+1}.")
            self.name_label = ctk.CTkLabel(frame, width=350, height=35, corner_radius=5, anchor=ctk.W, fg_color=colorpattern, text_color="#FFFFFF", font=small_font_mp, text=lb_pnames_pscores[i][0])
            self.score_label = ctk.CTkLabel(frame, width=125, height=35, corner_radius=5, anchor=ctk.E, fg_color=colorpattern, text_color="#FFFFFF", font=small_font_mp, text=lb_pnames_pscores[i][1])
            
            self.rank_label.pack(side=ctk.LEFT, padx=5, pady=5)
            self.name_label.pack(side=ctk.LEFT, padx=5)
            self.score_label.pack(side=ctk.LEFT, padx=5)

class EinstellungsPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self, text="Einstellungen", font=big_font_mp, text_color="#FFFFFF")
        self.label2.pack(pady=20)
        self.button = ctk.CTkButton(self, text="zurück", command=lambda: switch_callback(MainPage))
        self.button.pack(pady=10)


class SpielernamenPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        # Labels
        self.title = ctk.CTkLabel(self, text="Spielernamen eingeben", font=big_font_mp, text_color="#FFFFFF")
        self.title.pack(pady=20)

        # Inputs
        self.playername_1_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 1")
        self.playername_1_input.pack(pady=15)
        self.playername_2_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 2")
        self.playername_2_input.pack(pady=15)
        self.playername_3_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 3")
        self.playername_3_input.pack(pady=15)
        self.playername_4_input = ctk.CTkEntry(self, width=350, height=50, corner_radius=15, fg_color="#4F5165", font=medium_font_mp, text_color="#FFFFFF", placeholder_text="Spielername 4")
        self.playername_4_input.pack(pady=15)
        self.disableInputs()

        # Buttons
        self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(MainPage), self.clearPlayercount(), self.clearLeaderboard()])
        self.back_button.pack(pady=10, anchor=ctk.CENTER,side=ctk.BOTTOM)
        self.forward_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="weiter", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(HindernissPage), self.getSpielernamen(), self.createListOfCurrentPlayers()])
        self.forward_button.pack(pady=10, anchor=ctk.CENTER,side=ctk.BOTTOM)

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
        print("Create LB WTFFFFFF")
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
        self.label2 = ctk.CTkLabel(self, text="Hindernissplan", font=big_font_mp, text_color="#FFFFFF")
        self.label2.pack(pady=20)

        # Buttons
        self.back_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="zurück", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(SpielernamenPage))
        self.back_button.pack(pady=10)
        self.startgame_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Spiel starten", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(SpielPage), self.updateStatus()])
        self.startgame_button.pack(pady=10)
        self.info_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Info", text_color="#FFFFFF", font=medium_font_mp, fg_color="#FF5757", hover_color="#CD0000", command=lambda: switch_callback(InfoPage))
        self.info_button.pack(pady=10)
    
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
        global current_player_name
        current_player_name = list_current_players_scores[players_played_counter][0]
        print("create Spielpage")
        print("List:" + str(list_current_players_scores))

        # Labels
        self.points_label = ctk.CTkLabel(self, text=f"Punkte: {score}")
        self.points_label.place(x=330, y=40)
        self.currentplayer_label = ctk.CTkLabel(self, text=current_player_name)
        self.currentplayer_label.place(x=60, y=40)
        self.round_label = ctk.CTkLabel(self, text=f"Runde {round_number}/3")
        self.round_label.place(x=60, y=85)

        #self.goal_image = ctk.CTkImage(light_image=Image.open("icons\jakkolo_goal.png"), dark_image=Image.open("icons\jakkolo_goal.png"), size=(740, 224))
        self.goal_image_org = Image.open("icons\jakkolo_goal.png")
        self.resized_goal_image = self.goal_image_org.resize((1480, 448))
        self.goal_image = ImageTk.PhotoImage(self.resized_goal_image)
        self.canvas = ctk.CTkCanvas(self, width=1480, height=448, background="#474044", highlightthickness=0)
        self.canvas.place(x=150, y=300)
        self.canvas.create_image(740, 224, anchor=ctk.CENTER, image=self.goal_image)
        

        #self.goal_image = ctk.CTkImage(light_image=Image.open("icons\jakkolo_goal.png"), dark_image=Image.open("icons\jakkolo_goal.png"), size=(740, 224))
        #self.goal_label = ctk.CTkLabel(self, image=self.goal_image, text="")
        #self.goal_label.pack()
        

        
        

        # Labels for pucks in each target
        self.count_ones_label = ctk.CTkLabel(self.canvas, text=count_ones, font=medium_font_mp)
        self.count_ones_label.place(x=105, y=180)
        self.count_twos_label = ctk.CTkLabel(self.canvas, text=count_twos, font=medium_font_mp)
        self.count_twos_label.place(x=275, y=180)
        self.count_threes_label = ctk.CTkLabel(self.canvas, text=count_threes, font=medium_font_mp)
        self.count_threes_label.place(x=445, y=180)
        self.count_fours_label = ctk.CTkLabel(self.canvas, text=count_fours, font=medium_font_mp)
        self.count_fours_label.place(x=615, y=180)

        # Label for puck count
        self.puck_count_label = ctk.CTkLabel(self, text=f"Verbleibende Pucks: {puck_count}")
        self.puck_count_label.place(x=600, y=40)

        # Buttons
        self.showContinueOrFinishButton(switch_callback)
        #self.closeround_button = ctk.CTkButton(self, text="Ich schliesse Runde X von 3 ab", command=lambda: [switch_callback(RundenPage), self.increaseRoundnumber()])
        #self.closeround_button.pack(pady=10)
        self.explain_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Anleitung", text_color="#000000", font=small_font_mp, fg_color="pink", hover_color="#828282", command=lambda: switch_callback(AnleitungsPage))
        self.explain_button.place(x=440, y=510)
        self.endgame_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Spiel abbrechen", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(MainPage), self.updateStatus(), self.clearLeaderboard()])
        self.endgame_button.place(x=776, y=510)
        
        print("Players playeD:" + str(players_played_counter))

        self.after(250, self.update_variable)

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
        self.points_label.configure(text=score)
        self.after(250, self.update_variable)


    def updateStatus(self):
        global inGame
        inGame = False
        global round_number
        round_number = 1

    def resetRoundnumber(self):
        global round_number
        round_number = 1
        

    def clearLeaderboard(self):
        global list_current_players_scores
        list_current_players_scores.clear()

    def increaseRoundnumber(self):
        global round_number
        if round_number < 3:
            round_number += 1
        else:
            round_number = 1

    def showContinueOrFinishButton(self, switch_callback):
        global round_number
        if round_number < 3:
            self.closeround_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text=f"Ich schliesse Runde {round_number} von 3 ab", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(RundenPage), self.increaseRoundnumber()])
            self.closeround_button.place(x=55, y=510)
        else:      
            self.checkIfThereAreMorePlayers(switch_callback)
            self.resetRoundnumber()

    def createCurrentLeaderboard(self):
        global list_current_players_scores     
        global lb_pnames_pscores
        global players_played_counter
        self.updateScore()

        print("Before Current:")
        print(list_current_players_scores)
        print("Before lb:")
        print(lb_pnames_pscores)


        for i in range(len(list_current_players_scores)):
            for j in range(len(lb_pnames_pscores)):
                if list_current_players_scores[i][1] > lb_pnames_pscores[j][1]:
                    lb_pnames_pscores.insert(j, list_current_players_scores[i])
                    break
        players_played_counter = 0

    def checkIfThereAreMorePlayers(self, switch_callback):
        global players_played_counter
        if players_played_counter < player_count-1:
            self.endplayerturn_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25,text="Ich beende meine Spielzüge, nächster Spieler ist dran", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [switch_callback(RundenPage), self.resetRoundnumber(), self.updateScore()])
            self.endplayerturn_button.place(x=100, y=300)
        else:      
            self.endplayerturn_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25,text="Spiel ganz abschliessen", text_color="#000000", font=small_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [self.createCurrentLeaderboard(), switch_callback(ResultatPage), self.updateStatus(), self.resetRoundnumber()])
            self.endplayerturn_button.place(x=100, y=300)

    def updateScore(self):
        print("kappa")
        global players_played_counter, score, list_current_players_scores
        self.calculateScore()
        print(players_played_counter)
        list_current_players_scores[players_played_counter] = (current_player_name, score)
        keycounter.var1 = 0
        keycounter.var2 = 0
        keycounter.var3 = 0
        keycounter.var4 = 0
        score = 0        
        players_played_counter += 1

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
        global list_current_players_scores
        global lb_pnames_pscores
        
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
        self.stop_button = ctk.CTkButton(self, text="Beenden", command=lambda: [switch_callback(MainPage), self.updateStatus()])
        self.stop_button.pack(pady=10)
        self.leaderboard_button = ctk.CTkButton(self, text="Bestenliste", command=lambda: switch_callback(BestenlistPage))
        self.leaderboard_button.pack(pady=10)

    def updateStatus(self):
        global list_current_players_scores
        list_current_players_scores.clear()
        

class InfoPage(ctk.CTkFrame):
    def __init__(self, parent, switch_callback, fg_color, width, height):
        ctk.CTkFrame.__init__(self, width=width, height=height, master=parent, fg_color=fg_color)
        self.parent = parent
        
        # Labels
        self.label2 = ctk.CTkLabel(self, text="Info", font=big_font_mp, text_color="#FFFFFF")
        self.label2.pack(pady=20)

        # Buttons
        self.again_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="OK", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: switch_callback(HindernissPage))
        self.again_button.pack(pady=5, anchor=ctk.CENTER,side=ctk.BOTTOM)

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
        self.label2 = ctk.CTkLabel(self, text="Zwischen Runden Page", font=big_font_mp, text_color="#FFFFFF")
        self.label2.pack(pady=20)

        # Buttons
        self.again_button = ctk.CTkButton(master=self, width=130, height=60, corner_radius=25, text="Pucks eingesammelt", text_color="#FFFFFF", font=medium_font_mp, fg_color="#D9D9D9", hover_color="#828282", command=lambda: [self.recalculateCount(), switch_callback(SpielPage)])
        self.again_button.pack(pady=5, anchor=ctk.CENTER,side=ctk.BOTTOM)

    def recalculateCount(self):
        keycounter.var1 = self.ones_before_pause - self.ones_during_pause
        keycounter.var2 = self.twos_before_pause - self.threes_during_pause
        keycounter.var3 = self.threes_before_pause - self.threes_during_pause
        keycounter.var4 = self.fours_before_pause - self.fours_during_pause