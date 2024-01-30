from tkinter import *
root=Tk()
root.geometry("100x225")
class Frame(Tk):
    def __init__(self):
        super().__init__()
        self.l1 = Label(text="", width=10)
        self.e1 = Entry(width=10, justify=CENTER)
colors = {
"красный": "#ff0000",
"оранжевый": "#ff7d00",
"желтый": "#ffff00",
"зеленый": "#00ff00",
"голубой": "#007dff",
"синий": "#0000ff",
"фиолетовый": "#7d00ff"
}
def on_button_click(color_name, color_code):
    color_label.config(text=color_name)
    text_field.delete(1.0, END)
    text_field.insert(END, color_code)

color_label = Label(root, text="", font=(16))
color_label.pack()
text_field = Text(root, height=1, width=10, font=(16))
text_field.pack()
for color_name, color_code in colors.items():
    button = Button(root, width=50, text=color_name,
    bg=color_code,command=lambda name=color_name, code=color_code:
    on_button_click(name, code))
    button.pack()
root.mainloop()