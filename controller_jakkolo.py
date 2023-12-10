import customtkinter as ctk
from pages.pages_jakkolo import MainPage, AnleitungsPage

class App(ctk.CTk):
    def __init__(self, root):
        self.root = root
        self.root.title("Titelblatt")
        self.root.geometry("1024x600")
        self.root.resizable(False, False)

        self.current_frame = None
        self.show_first_page()

    def show_first_page(self):
        self.switch_frame(MainPage)
    """ 
    def show_second_page(self):
        self.switch_frame(AnleitungsPage)
    """
    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame_class(self.root, self.switch_frame)
        self.current_frame.pack(padx=20, pady=20)  # Display the new frame
