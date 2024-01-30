from tkinter import *
from tkinter import filedialog, messagebox
def open_file():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text.delete('1.0', END)
                text.insert(END, file.read())
    except FileNotFoundError:
        messagebox.showinfo("Ошибка", "Файл не загружен")
def save_file():
    try:
        file_path = filedialog.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),("HTML files", "*.html;*.htm"),("All files", "*.*")))
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get('1.0', END))
    except FileNotFoundError:
        messagebox.showinfo("Ошибка", "Файл не сохранен")
def clear_text():
    result = messagebox.askquestion("Подтверждение", "Вы уверены, что хотите очистить текст?")
    if result == 'yes':
        text.delete('1.0', END)
root = Tk()
root.geometry('500x500')
text = Text(root, width=50, height=25)
text.pack()
open_button = Button(root, text="Открыть", command=open_file)
open_button.pack(side=LEFT)
save_button =Button(root, text="Сохранить", command=save_file)
save_button.pack(side=LEFT)
clear_button = Button(root, text="Очистить", command=clear_text)
clear_button.pack(side=LEFT)
root.mainloop()