from tkinter import *

class AnimationApp:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.rect = self.canvas.create_rectangle(50, 50, 100, 100, fill="pink")
        self.dx = 0
        self.dy = 0

        self.speed_scale = Scale(master, from_=1, to=50, orient=HORIZONTAL, label="Скорость", command=self.set_speed)
        self.speed_scale.pack()

        self.master.bind("<Up>", lambda event: self.move(0, -5))
        self.master.bind("<Down>", lambda event: self.move(0, 5))
        self.master.bind("<Left>", lambda event: self.move(-5, 0))
        self.master.bind("<Right>", lambda event: self.move(5, 0))

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.animate()

    def animate(self):

        x1, y1, x2, y2 = self.canvas.coords(self.rect)

        new_x1 = x1 + self.dx
        new_y1 = y1 + self.dy
        new_x2 = x2 + self.dx
        new_y2 = y2 + self.dy

        if new_x1 >= 0 and new_y1 >= 0 and new_x2 <= 400 and new_y2 <= 400:
            self.canvas.move(self.rect, self.dx, self.dy)

            self.master.after(100 // self.speed_scale.get(), self.animate)

    def set_speed(self, value):
        pass

root = Tk()
app = AnimationApp(root)
root.mainloop()
