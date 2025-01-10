import customtkinter as ctk
from laser import startLaser, stopLaser

# Create App class
class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        stopLaser()
        super().__init__(*args, **kwargs)
        self.isLaser = False
        # Sets the title of our window to "App"
        self.title("App")    
        # Dimensions of the window will be 200x200
        self.geometry("400x200")    

        self.label = ctk.CTkLabel(self, text="Label")
        self.label.pack()
        self.button = ctk.CTkButton(self, text="Test", command=self.laser)
        self.button.pack()

    def laser(self):
        if not self.isLaser:
            startLaser()
            self.isLaser = True
        else:
            stopLaser()
            self.isLaser = False
         

if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()   
