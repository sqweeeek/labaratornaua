from tkinter import *
def draw_house():
    canvas.create_rectangle(100, 200, 300, 400, outline="black", fill="lightblue")
    canvas.create_polygon(100, 200, 200, 100, 300, 200, outline="black",fill="light blue")
def draw_grass():
    for i in range(10):
        canvas.create_rectangle(i*50, 400, (i+1)*50, 460, outline="green",fill="green")
def draw_sun():
    canvas.create_oval(350,40, 430, 120, outline="orange", fill="orange")
root = Tk()
root.title("tk")
canvas = Canvas(root, width=430, height=430)
canvas.pack()
draw_house()
draw_grass()
draw_sun()
root.mainloop()