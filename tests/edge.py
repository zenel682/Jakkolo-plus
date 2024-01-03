import tkinter as tk

def open_singleplayer():
    singleplayer_window = tk.Toplevel()
    singleplayer_window.title("Singleplayer")
    singleplayer_window.geometry("200x200")
    singleplayer_window.mainloop()

def open_2spieler():
    spieler_window = tk.Toplevel()
    spieler_window.title("2 Spieler")
    spieler_window.geometry("200x200")
    spieler_window.mainloop()

def open_3spieler():
    spieler_window = tk.Toplevel()
    spieler_window.title("3 Spieler")
    spieler_window.geometry("200x200")
    spieler_window.mainloop()

def open_4spieler():
    spieler_window = tk.Toplevel()
    spieler_window.title("4 Spieler")
    spieler_window.geometry("200x200")
    spieler_window.mainloop()

def open_start():
    start_window = tk.Toplevel()
    start_window.title("Start")
    start_window.geometry("200x200")
    start_window.mainloop()

def open_anleitung():
    anleitung_window = tk.Toplevel()
    anleitung_window.title("Anleitung")
    anleitung_window.geometry("200x200")
    anleitung_window.mainloop()

def open_bestenliste():
    bestenliste_window = tk.Toplevel()
    bestenliste_window.title("Bestenliste")
    bestenliste_window.geometry("200x200")
    bestenliste_window.mainloop()

root = tk.Tk()
root.title("Jakkolo plus")
root.geometry("300x300")
root.configure(bg='#FFDAB9')

title_label = tk.Label(root, text="Jakkolo plus", font=("Arial", 20), bg='#FFDAB9')
title_label.grid(row=0, column=0)

singleplayer_button = tk.Button(root, text="Singleplayer", bg='#800080', fg='white', command=open_singleplayer)
singleplayer_button.grid(row=1, column=0)

spieler_button = tk.Button(root, text="2 Spieler", bg='#800080', fg='white', command=open_2spieler)
spieler_button.grid(row=2, column=0)

spieler_button = tk.Button(root, text="3 Spieler", bg='#800080', fg='white', command=open_3spieler)
spieler_button.grid(row=3, column=0)

spieler_button = tk.Button(root, text="4 Spieler", bg='#800080', fg='white', command=open_4spieler)
spieler_button.grid(row=4, column=0)

start_button = tk.Button(root, text="Start", bg='#FFA500', fg='white', command=open_start)
start_button.grid(row=1, column=1)

anleitung_button = tk.Button(root, text="Anleitung", bg='#FFA500', fg='white', command=open_anleitung)
anleitung_button.grid(row=2, column=1)

bestenliste_button = tk.Button(root, text="Bestenliste", bg='#FFA500', fg='white', command=open_bestenliste)
bestenliste_button.grid(row=3, column=1)

cogwheel_image = tk.PhotoImage(file="gear.png")
cogwheel_label = tk.Label(root, image=cogwheel_image, bg='#FFDAB9')
cogwheel_label.grid(row=0, column=2)

root.mainloop()
