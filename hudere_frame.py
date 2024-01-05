import tkinter as tk

class HudereFrame:
    def __init__(self, master, title, bg_color):
        self.master = master
        self.frame = tk.Frame(master, bg=bg_color)

        # Top Title inside the frame
        title_label = tk.Label(self.frame, text=title, font=("Helvetica", 24), bg=bg_color, fg="white")
        title_label.pack(pady=10)

        # Wider button on the left under the title
        left_button = tk.Button(self.frame, text="Wide Button", width=20, bg=bg_color, fg="white")
        left_button.pack(side=tk.LEFT, padx=10)

        # Smaller button on the right under the title
        right_button = tk.Button(self.frame, text="Small Button", width=10, bg=bg_color, fg="white")
        right_button.pack(side=tk.RIGHT, padx=10)

        # 3 buttons in the middle
        middle_button1 = tk.Button(self.frame, text="Button 1", width=15, bg=bg_color, fg="white")
        middle_button2 = tk.Button(self.frame, text="Button 2", width=15, bg=bg_color, fg="white")
        middle_button3 = tk.Button(self.frame, text="Button 3", width=15, bg=bg_color, fg="white")

        middle_button1.pack(pady=10)
        middle_button2.pack(pady=10)
        middle_button3.pack(pady=10)
