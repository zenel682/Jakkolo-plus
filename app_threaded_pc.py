import threading
import tkinter as tk
import customtkinter as ctk
from tkinter import font
import atexit

# Toogle when using Raspi or PC
#from gpio_class import Endschalter
#endschalter = Endschalter()
#thread1 = threading.Thread(target=endschalter.read_endschalter)

from keyboard_class import KeyCounter
keycounter = KeyCounter()
thread1 = threading.Thread(target=keycounter)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.root = root
        self.title("Button Page Example")
        self.configure(bg="#E6E6FA")  # Set light purple background color
        self.new_value = 0
        self.start = False

        # Set the default font for the buttons
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Helvetica", size=12, weight="bold")

        # Set the window size and make it unscalable
        self.geometry("1024x600")
        self.resizable(False, False)
        #self.root.config(cursor="none")

        # Create normal style buttons
        self.start_button = ctk.CTkButton(
            self,
            text="Start",
            command=lambda: self.show_page("Start"),
            fg_color="white",
            font=("Helvetica", 12, "bold"),
        )
        self.start_button.pack(ipadx=10, padx=20)

        self.leaderboard_button = ctk.CTkButton(
            self,
            text="Leaderboard",
            command=lambda: self.show_page("Leaderboard"),
            border_color="#FFA500",
            fg_color="white",
            font=("Helvetica", 12, "bold"),
        )
        self.leaderboard_button.pack(ipadx=10, padx=20)

        self.explanation_button = ctk.CTkButton(
            self,
            text="Explanation",
            command=lambda: self.show_page("Explanation"),
            border_color="#FFA500",
            fg_color="white",
            font=("Helvetica", 12, "bold"),
        )
        self.explanation_button.pack(ipadx=10, padx=20)

        # Start tracker button
        self.tracker_start = ctk.CTkButton(
            self,
            text="Start tracker",
            command=lambda: self.start_tracker(),
            border_color="#FFA500",
            fg_color="white",
            font=("Helvetica", 12, "bold"),
        )
        self.tracker_start.pack(ipadx=10, padx=20)

        # Stop tracker button
        self.tracker_stop = ctk.CTkButton(
            self,
            text="Stop tracker",
            command=lambda: self.stop_tracker(),
            border_color="#FFA500",
            fg_color="white",
            font=("Helvetica", 12, "bold"),
        )
        self.tracker_stop.pack(ipadx=10, padx=20)

        # Add labels
        # Variable to be displayed in the label
        self.display_var1 = tk.IntVar()
        self.display_var1.set(0)
        self.display_var2 = tk.IntVar()
        self.display_var2.set(0)
        self.display_var3 = tk.IntVar()
        self.display_var3.set(0)
        self.display_var4 = tk.IntVar()
        self.display_var4.set(0)

        # Label1 to display the variable
        self.display_label1 = tk.Label(
            self,
            textvariable=self.display_var1,
            font=("Helvetica", 14),
        )
        self.display_label1.pack(padx=0, pady=20)

        # Label2 to display the variable
        self.display_label2 = ctk.CTkLabel(
            self,
            textvariable=self.display_var2,
            font=("Helvetica", 14),
        )
        self.display_label2.pack(padx=10, pady=20)

        # Label3 to display the variable
        self.display_label3 = ctk.CTkLabel(
            self,
            textvariable=self.display_var3,
            font=("Helvetica", 14),
        )
        self.display_label3.pack(padx=20, pady=20)

        # Label4 to display the variable
        self.display_label4 = ctk.CTkLabel(
            self,
            textvariable=self.display_var4,
            font=("Helvetica", 14),
        )
        self.display_label4.pack(padx=30, pady=20)

        # Frame to display content
        self.current_frame = ctk.CTkFrame(self)  # Set light purple background color

        # Schedule the update function to run every 1000 milliseconds (1 second)
        self.after(1000, self.update_variable)

    def start_tracker(self):
        print("Start Tracking")
        # Toggle on Raspi or PC
        #self.display_var = endschalter.b1_counter
        #endschalter.read_it = True  
        try: 
            self.thread1 = threading.Thread(target=self.run_keycounter)
            self.thread1.start()
            self.start = True
            print("thread started")
            #self.display_var = run
            
        #    keycounter.readKeys = True
        #    thread1.start()
        except:
            print("Already openend thread")
    def run_keycounter(self):    
        self.keycounter = KeyCounter()
        self.keycounter.run()
        
    #def read_gpio(self):
    #    self.endschalter = Endschalter()
    #    self.endschalter.read_endschalter()

    def stop_tracker(self):
        if self.thread1 and self.thread1.is_alive():
            #self.endschalter.stop()
            self.keycounter.stop()
            self.thread1.join(timeout=3)
            print("Joined threads")
        else:
            print("Thread was not opened yet")

    # Update score variable
    def update_variable(self):
        # Toggle Raspi and PC
        #new_value = endschalter.b1_counter
        if self.start:
            print("keycounter there") 
            #new_value1= self.endschalter.b1_counter
            #new_value2= self.endschalter.b2_counter
            #new_value3= self.endschalter.b3_counter
            #new_value4= self.endschalter.b4_counter
            new_value1= self.keycounter.var1
            new_value2= self.keycounter.var2
            new_value3= self.keycounter.var3
            new_value4= self.keycounter.var4
        else: 
            print("no keycounter")
            new_value1 = 0
            new_value2 = 0
            new_value3 = 0
            new_value4 = 0

        self.display_var1.set(new_value1)
        self.display_var2.set(new_value2)
        self.display_var3.set(new_value3)
        self.display_var4.set(new_value4)

        # Schedule the update function to run again after 1000 milliseconds
        self.after(100, self.update_variable)

    def show_page(self, title):
        # Destroy any existing widgets in the current frame
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        # Display the title in the current frame
        title_label = ctk.CTkLabel(self.current_frame, text=title, font=("Helvetica", 16, "bold"))
        title_label.pack()

        # Button to go back to the main frame
        back_button = ctk.CTkButton(
            self.current_frame,
            text="Back to Main",
            command=self.show_main_page,
            fg_color="white",
            font=("Helvetica", 12, "bold"),
        )
        back_button.pack()

        #self.add_hover_effect(back_button)

        # Hide the main buttons
        self.start_button.pack_forget()
        self.leaderboard_button.pack_forget()
        self.explanation_button.pack_forget()
        self.tracker_start.pack_forget()
        self.tracker_stop.pack_forget()
        self.display_label1.pack_forget()
        self.display_label2.pack_forget()
        self.display_label3.pack_forget()
        self.display_label4.pack_forget()

        if title == "Start":
            print("Dood bob")
            self.start_page()

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
        self.tracker_start.pack(ipadx=10, padx=20)
        self.tracker_stop.pack(ipadx=10, padx=20)
        self.display_label1.pack(ipadx=0, padx=20)
        self.display_label2.pack(ipadx=10, padx=20)
        self.display_label3.pack(ipadx=20, padx=20)
        self.display_label4.pack(ipadx=30, padx=20)

        # Unpack the current frame to hide it
        self.current_frame.pack_forget()
    
    def stop_threads(self):
        self.stop_tracker()
        # Add more cleanup if needed

    def start_page(self):
         # Test label to display the variable
        self.testlabel = ctk.CTkLabel(
            self,
            textvariable="OKIDOKI",
            font=("Helvetica", 30),
        )
        self.testlabel.pack(padx=30, pady=20)

if __name__ == "__main__":
    app = App()
    #app = App(root)
    # Register cleanup function
    atexit.register(app.stop_threads)
    app.mainloop()
