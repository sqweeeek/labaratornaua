from tkinter import *
def open_file():
    file_path = entry.get()
    with open(file_path, 'r') as file:
        content = file.read()
        text.delete(1.0, END)
        text.insert(END, content)
def save_file():
    file_path = entry.get()
    content = text.get(1.0, END)
    with open(file_path, 'w') as file:
        file.write(content)
root = Tk()
root.title("tk")
label = Label(root)
label.pack()
entry = Entry(root)
entry.pack()
text = Text(root)
text.pack()
open_button = Button(root, text="Открыть", command=open_file)
open_button.pack()
save_button = Button(root, text="Сохранить", command=save_file)
save_button.pack()
root.mainloop()