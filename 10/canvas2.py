from tkinter import *
def move_to_click(event):
    x, y = event.x, event.y
    current_x, current_y = c.coords(ball)[0], c.coords(ball)[1]
    if current_x < x:
       c.move(ball, 1, 0)
    elif current_x > x:
        c.move(ball, -1, 0)
    if current_y < y:
        c.move(ball, 0, 1)
    elif current_y > y:
        c.move(ball, 0, -1)
    if (current_x, current_y) != (x, y):
        root.after(10, lambda: move_to_click(event))
root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='green')
c.bind("<Button-1>", move_to_click)
root.mainloop()