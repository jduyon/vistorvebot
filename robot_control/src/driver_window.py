from tkinter import *

root = Tk()

def key(event):
    print (event.keysym)

def callback(event):
    frame.focus_set()
    print ("clicked", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
print ("hello")
root.mainloop()
