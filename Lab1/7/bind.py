from tkinter import *
def add(event):
    text = entry.get()
    if text:
        lbox.insert(END, text)
        entry.delete(0, END)
def copy(event):
    item = lbox.get(ACTIVE)
    entry.insert(END, item)
root = Tk()
root.title("")
entry = Entry(root)
entry.bind("<Return>", add)
entry.pack()
lbox = Listbox(root)
lbox.bind("<Double-Button-1>", copy)
lbox.pack()
root.mainloop()