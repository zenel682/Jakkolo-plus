import pyglet,tkinter
pyglet.font.add_file('fonts\LeagueSpartan-ExtraBold.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root,text="test",font=('LeagueSpartan-ExtraBold',25))
MyLabel.pack()
root.mainloop()
