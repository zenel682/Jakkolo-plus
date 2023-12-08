import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Continuous Label Update")

        self.label_var = tk.StringVar()
        self.label_var.set("Initial Text")

        self.label = tk.Label(root, textvariable=self.label_var, font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Call the update_label method every 1000 milliseconds (1 second)
        self.root.after(1000, self.update_label)

    def update_label(self):
        # Update the label text here
        new_text = 1
        self.label_var.set(new_text)

        # Call the update_label method again after 1000 milliseconds
        self.root.after(1000, self.update_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
