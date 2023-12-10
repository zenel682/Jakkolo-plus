import customtkinter as ctk
from pages.pages import MyFrame, SecondFrame

class App(ctk.CTk):
    def __init__(self, root):
        self.root = root
        self.root.title("Titelblatt")

        self.current_frame = None
        self.show_first_page()

    def show_first_page(self):
        self.switch_frame(MyFrame)

    def show_second_page(self):
        self.switch_frame(SecondFrame)

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame_class(self.root, self.switch_frame)
        self.current_frame.pack(padx=20, pady=20)  # Display the new frame
