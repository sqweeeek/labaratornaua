from tkinter import *
def add_figure_window():
     add_window = Toplevel(root)
     x1_label = Label(add_window, text="x1:")
     x1_label.grid(row=0, column=0)
     x1_entry = Entry(add_window)
     x1_entry.grid(row=0, column=1)
     y1_label = Label(add_window, text="y1:")
     y1_label.grid(row=1, column=0)
     y1_entry = Entry(add_window)
     y1_entry.grid(row=1, column=1)
     x2_label = Label(add_window, text="x2:")
     x2_label.grid(row=2, column=0)
     x2_entry = Entry(add_window)
     x2_entry.grid(row=2, column=1)
     y2_label = Label(add_window, text="y2:")
     y2_label.grid(row=3, column=0)
     y2_entry = Entry(add_window)
     y2_entry.grid(row=3, column=1)
     figure_type = StringVar()
     pryam_radio = Radiobutton(add_window, text="Прямоугольник",
    variable=figure_type, value="Прямоугольник")
     pryam_radio.grid(row=4, column=0)
     oval_radio =Radiobutton(add_window, text="Овал", variable=figure_type,
    value="Овал")
     oval_radio.grid(row=4, column=1)
     button = Button(add_window, text="Нарисовать", command=lambda:
    draw_figure(x1_entry.get(), y1_entry.get(), x2_entry.get(), y2_entry.get(),
    figure_type.get()))
     button.grid(row=5, columnspan=2)
def draw_figure(x1, y1, x2, y2, figure_type):
    if figure_type == "Прямоугольник":
        canvas.create_rectangle(int(x1), int(y1), int(x1) + int(x2), int(y1) + int(y2))
    elif figure_type == "Овал":
        canvas.create_oval(int(x1), int(y1), int(x1) + int(x2), int(y1) + int(y2))
root = Tk()

root.title("Прямовал")
canvas = Canvas(root, width=400, height=400)
canvas.pack()
add_button = Button(root, text="Добавить фигуру", command=add_figure_window)
add_button.pack()

root.mainloop()