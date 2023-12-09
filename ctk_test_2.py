import customtkinter as ctk

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master, switch_callback)
        self.master = master

        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
        self.button = ctk.CTkButton(self, command=lambda: switch_callback(SecondFrame))
        self.button.grid(row=1, column=1)

    def showframe(self):
        self.frame = SecondFrame(master=self, switch_callback=self.switch_callback)
        print("Test")

class SecondFrame(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master, switch_callback)

        self.label2 = ctk.CTkLabel(self)
        self.label2.grid(row=5, column=4)
        self.button = ctk.CTkButton(self, command=lambda: switch_callback(MyFrame))
        self.button.grid(row=1, column=1)

class App(ctk.CTk):
    def __init__(self, master):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.master = master

        self.current_frame = None
        self.show_first_page()

        self.my_frame = MyFrame(master=self, switch_callback=self.switch_frame)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def show_first_page(self):
        self.switch_frame(MyFrame)

    def show_second_page(self):
        self.switch_frame(SecondFrame)

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame_class(self.master, self.switch_frame)
        self.current_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Display the new frame

if __name__ == "__main__":
    master = ctk.CTk()
    app = App(master)
    app.mainloop()