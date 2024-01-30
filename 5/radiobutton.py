from tkinter import *
def show_select():
    selected_option = var.get()
    if selected_option == 1:
        label.config(text="8 800 555 35 35")
    elif selected_option == 2:
        label.config(text="+4 9087654321")
    elif selected_option == 3:
        label.config(text="8 800 666 66 66")
root = Tk()
var = IntVar()
r1 = Radiobutton(root, text="Домашний кредит", variable=var, value=1,
indicatoron=0, command=show_select)
r1.pack(anchor='w')
r2 = Radiobutton(root, text="Петя", variable=var, value=2, indicatoron=0,
command=show_select)
r2.pack(anchor='w')
r3 = Radiobutton(root, text="Сантекник Вася", variable=var, value=3,
indicatoron=0, command=show_select)
r3.pack(anchor='w')
label = Label(root, width=30)
label.pack()
root.mainloop()