from tkinter import *
def move_list():
    selected_items = entry.curselection()
    for item in selected_items:
        box2.insert(END, entry.get(item))
        entry.delete(item)
def move_back():
    items = box2.curselection()
    for i in items:
        entry.insert(END, box2.get(i))
        box2.delete(i)
root = Tk()
root.title("Список покупок")
products = ["Яблоки", "Бананы", "Морковь", "Хлеб", "Масло",
"Мяско","Картошка","АНАНАС"]
shopping_list = []
f = Frame()
f.pack(side=RIGHT, padx=10)
entry = Listbox(root, selectmode=EXTENDED)
for product in products:
    entry.insert(END, product)
entry.pack(side=LEFT)
box2 = Listbox(f, selectmode=EXTENDED)
box2.pack(side=RIGHT)
add_button = Button(f, text=">>>", command=move_list)
add_button.pack()
remove_button = Button(f, text="<<<", command=move_back)
remove_button.pack()
root.mainloop()