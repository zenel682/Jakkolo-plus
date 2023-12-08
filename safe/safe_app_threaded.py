import threading
import tkinter as tk
from tkinter import font
import atexit

# Toogle when using Raspi or PC
#from gpio_class import Endschalter
#endschalter = Endschalter()
#thread1 = threading.Thread(target=endschalter.read_endschalter)

from keyboard_class import KeyCounter
#keycounter = KeyCounter()
#thread1 = threading.Thread(target=keycounter)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Page Example")
        self.root.configure(bg="#E6E6FA")  # Set light purple background color
        self.new_value = 0
        self.start = False

        # Set the default font for the buttons
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Helvetica", size=12, weight="bold")

        # Set the window size and make it unscalable
        self.root.geometry("1024x600")
        self.root.resizable(False, False)

        # Create normal style buttons
        self.start_button = tk.Button(
            root,
            text="Start",
            command=lambda: self.show_page("Start"),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.start_button.pack(ipadx=10, padx=20)

        self.add_hover_effect(self.start_button)

        self.leaderboard_button = tk.Button(
            root,
            text="Leaderboard",
            command=lambda: self.show_page("Leaderboard"),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.leaderboard_button.pack(ipadx=10, padx=20)
        self.add_hover_effect(self.leaderboard_button)

        self.explanation_button = tk.Button(
            root,
            text="Explanation",
            command=lambda: self.show_page("Explanation"),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.explanation_button.pack(ipadx=10, padx=20)
        self.add_hover_effect(self.explanation_button)

        # Start tracker button
        self.tracker_start = tk.Button(
            root,
            text="Start tracker",
            command=lambda: self.start_tracker(),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.tracker_start.pack(ipadx=10, padx=20)
        self.add_hover_effect(self.tracker_start)

        # Stop tracker button
        self.tracker_stop = tk.Button(
            root,
            text="Stop tracker",
            command=lambda: self.stop_tracker(),
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        self.tracker_stop.pack(ipadx=10, padx=20)
        self.add_hover_effect(self.tracker_stop)

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
            root,
            textvariable=self.display_var1,
            font=("Helvetica", 14),
            bg="#E6E6FA"
        )
        self.display_label1.pack(padx=0, pady=20)

        # Label2 to display the variable
        self.display_label2 = tk.Label(
            root,
            textvariable=self.display_var2,
            font=("Helvetica", 14),
            bg="#E6E6FA"
        )
        self.display_label2.pack(padx=10, pady=20)

        # Label3 to display the variable
        self.display_label3 = tk.Label(
            root,
            textvariable=self.display_var3,
            font=("Helvetica", 14),
            bg="#E6E6FA"
        )
        self.display_label3.pack(padx=20, pady=20)

        # Label4 to display the variable
        self.display_label4 = tk.Label(
            root,
            textvariable=self.display_var4,
            font=("Helvetica", 14),
            bg="#E6E6FA"
        )
        self.display_label4.pack(padx=30, pady=20)

        # Frame to display content
        self.current_frame = tk.Frame(root, padx=20, pady=20, bg="#E6E6FA")  # Set light purple background color

        # Schedule the update function to run every 1000 milliseconds (1 second)
        self.root.after(1000, self.update_variable)
    def add_hover_effect(self, button):
        button.bind("<Enter>", lambda event, b=button: self.on_enter(event, b))
        button.bind("<Leave>", lambda event, b=button: self.on_leave(event, b))

    def on_enter(self, event, button):
        button.config(bg="#FFD700")  # Brighter color on hover

    def on_leave(self, event, button):
        button.config(bg="#FFA500")  # Restore original color on leave

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

    def stop_tracker(self):
        if self.thread1 and self.thread1.is_alive():
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
        self.root.after(1000, self.update_variable)

    def show_page(self, title):
        # Destroy any existing widgets in the current frame
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        # Display the title in the current frame
        title_label = tk.Label(self.current_frame, text=title, font=("Helvetica", 16, "bold"), bg="#E6E6FA")
        title_label.pack()

        # Button to go back to the main frame
        back_button = tk.Button(
            self.current_frame,
            text="Back to Main",
            command=self.show_main_page,
            bg="#FFA500",
            fg="white",
            font=("Helvetica", 12, "bold"),
        )
        back_button.pack()

        self.add_hover_effect(back_button)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    # Register cleanup function
    atexit.register(app.stop_threads)
    root.mainloop()
