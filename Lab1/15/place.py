from tkinter import *
from tkinter import PhotoImage
import random
def move_smiley():
    new_x = random.randint(0, root.winfo_width()-50) # Генерируем новые координаты x
    new_y = random.randint(0, root.winfo_height()-50) # Генерируем новые координаты y
    button.place(x=new_x, y=new_y) # Перемещаем кнопку на новые координаты

root = Tk()
root.title("смайл")
smiley_img = PhotoImage(file='C:\\Users\\user\\Downloads\\smile.gif')
button = Button(root, image=smiley_img, command=move_smiley)
button.pack()
root.mainloop()