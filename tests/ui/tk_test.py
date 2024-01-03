import tkinter as tk

def create_labels():
    root = tk.Tk()
    root.title("Labels with Side Labels")

    # Define the number of labels
    label_count = 5
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP)
    for i in range(label_count):
        # Create a frame for each row of three labels
        frame = tk.Frame(root)
        frame.pack(side=tk.TOP)

        # Create the main label for each row
        label_main = tk.Label(frame, text=f"Main Label {i+1}")
        label_main.pack(side=tk.LEFT)

        # Create two side labels for each row
        label_side1 = tk.Label(frame, text=f"Side Label 1 ({i+1})")
        label_side2 = tk.Label(frame, text=f"Side Label 2 ({i+1})")

        label_side1.pack(side=tk.LEFT, padx=5)  # padx adds horizontal spacing between labels
        label_side2.pack(side=tk.LEFT)

    root.mainloop()

create_labels()
