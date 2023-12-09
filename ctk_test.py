from typing import Optional, Tuple, Union
import customtkinter as ctk

class MyFrame(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent

        self.label = ctk.CTkLabel(self)
        self.label.pack(padx=20, pady=20)
        self.button = ctk.CTkButton(self, text="Go to Page 2", command=lambda: switch_callback(SecondFrame))
        self.button.pack(pady=10)

class SecondFrame(ctk.CTkFrame):
    def __init__(self, parent, switch_callback):
        ctk.CTkFrame.__init__(self, parent)
        self.parent = parent
        
        self.label2 = ctk.CTkLabel(self)
        self.label2.pack(pady=20)
        self.button = ctk.CTkButton(self, text="Return to Page 1", command=lambda: switch_callback(MyFrame))
        self.button.pack(pady=10)

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
