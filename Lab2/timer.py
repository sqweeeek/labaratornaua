from tkinter import *
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")


        self.min_l = Label(master, text="Минуты:")
        self.min_l.pack()
        self.min_e = Entry(master)
        self.min_e.pack()

        self.sec_l = Label(master, text="Секунды:")
        self.sec_l.pack()
        self.sec_e = Entry(master)
        self.sec_e.pack()

        start_button = Button(master, text="Начать", command=self.start_timer)
        start_button.pack()

    def start_timer(self):
        try:
            min = int(self.min_e.get())
            seconds = int(self.sec_e.get())
            total_seconds = min * 60 + seconds

            while total_seconds > 0:
                min, sec = divmod(total_seconds, 60)
                timeformat = '{:02d}:{:02d}'.format(min, sec)
                self.master.title("Время: " + timeformat)
                self.master.update()
                time.sleep(1)
                total_seconds -= 1

            messagebox.showinfo("Таймер завершен", "Время окончено!!")


        except ValueError:
            messagebox.showerror("Неправильно введены данные", "Ввидите верные данные")

root = Tk()
app = TimerApp(root)
root.mainloop()
