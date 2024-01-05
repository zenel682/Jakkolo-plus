import customtkinter as ctk
from pages_jakkolo_raspi import MainPage

class App(ctk.CTk):
    def __init__(self, root):
        self.root = root
        root.geometry("1024x600")
        #root.overrideredirect(True)
        root.configure(fg_color="#474044")

        self.current_frame = None
        self.show_first_page()

    def show_first_page(self):
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame_class(self.root, self.switch_frame, fg_color="#474044", width=1024, height=600)
        self.current_frame.pack()  # Display the new frame
