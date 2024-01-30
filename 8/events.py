from tkinter import *
def change_size(event=None):
    try:
        width = int(w_entry.get())
        height = int(h_entry.get())
        text.config(width=width, height=height)
    except ValueError:
        pass
def on_focus_in(event):
    text.config(bg="white")
def on_focus_out(event):
    text.config(bg="lightgrey")
root =Tk()
w_label = Label(root, text="Ширина:")
w_label.pack()
w_entry = Entry(root)
w_entry.pack()
h_label = Label(root, text="Высота:")
h_label.pack()
h_entry = Entry(root)
h_entry.pack()
button = Button(root, text="Изменить", command=change_size)
button.pack()
text = Text(root, bg="lightgrey")
text.pack()
text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)
root.mainloop()