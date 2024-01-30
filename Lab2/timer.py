from tkinter import *
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")
        self.master.configure(bg='lightblue')

        self.minl = Label(master, text="Минуты:")
        self.minl.pack()
        self.mine = Entry(master)
        self.mine.pack()

        self.secl = Label(master, text="Секунды:")
        self.secl.pack()
        self.sece= Entry(master)
        self.sece.pack()

        start_but = Button(master, text="Начало", command=self.start_timer)
        start_but.pack()

def start_timer(self):
    try:
        min = int(self.mine.get())
        sec = int(self.sece.get())
        total_sec = min * 60 + sec

        while total_sec > 0:
            minutes, sec = divmod(total_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(minutes, sec)
            self.master.title("Таймер: " + timeformat)
            self.master.update()
            time.sleep(1)
            total_sec-=1

    messagebox.showinfo("Таймер завершен", "Время окончено")
    expect ValueError:
messagebox.showerror("Неправильно введены данные", "Ввидите цифры данные.")


root = Tk()
app = TimerApp(root)
root.mainloop()