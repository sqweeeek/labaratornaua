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
menu_bar = Menu(root)
menu = Menu(menu_bar, tearoff=0)
menu.add_command(label="Открыть", command=open_file)
menu.add_command(label="Сохранить", command=save_file)
menu.add_separator()
menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=menu)
root.config(menu=menu_bar)
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Очистить", command=clear_text)
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)
text.bind("<Button-3>",show_context_menu )
root.mainloop()