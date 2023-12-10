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
