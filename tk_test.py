import tkinter as tk

class FirstPage(tk.Frame):
    def __init__(self, parent, switch_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        label = tk.Label(self, text="Page 1")
        label.pack(pady=20)

        button = tk.Button(self, text="Go to Page 2", command=lambda: switch_callback(SecondPage))
        button.pack(pady=10)

class SecondPage(tk.Frame):
    def __init__(self, parent, switch_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        label = tk.Label(self, text="U got it!")
        label.pack(pady=20)

        return_button = tk.Button(self, text="Return to Page 1", command=lambda: switch_callback(FirstPage))
        return_button.pack(pady=10)

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Switching")

        self.current_frame = None  # To keep track of the current frame

        self.show_first_page()

    def show_first_page(self):
        self.switch_frame(FirstPage)

    def show_second_page(self):
        self.switch_frame(SecondPage)

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame

        self.current_frame = frame_class(self.root, self.switch_frame)
        self.current_frame.pack()  # Display the new frame

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
