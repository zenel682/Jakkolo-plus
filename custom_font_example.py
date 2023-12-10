import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Custom Font Example")

# Load the TrueType Font (.ttf) file
custom_font_path = "path/to/your/font.ttf"
custom_font = ("CustomFont", 12)  # Specify the font family and size

# Create a ttk style and configure it to use the custom font
style = ttk.Style()
style.configure("Custom.TButton", font=custom_font)

# Create a button with the custom font
custom_button = ttk.Button(root, text="Click me!", style="Custom.TButton")
custom_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
