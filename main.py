from tkinter import *
# from tkinter import messagebox
from db import first_fiche,insert_todo,delete_todo



todo = []
todo = first_fiche()

def update_listbox():
    lb.delete('0','end')
    for item in todo:
        lb.insert(END, item)


def newTask():
    global todo
    task = my_entry.get()
    todo = insert_todo(task)
    update_listbox()
    my_entry.delete('0','end')


def deleteTask():
    global todo
    todo = delete_todo(todo[lb.curselection()[0]][0])

    update_listbox()



tk = Tk()
tk.geometry('1000x500')
tk.resizable(width=False, height=False)
tk.title('Todo List | Eslam Elnemery')
tk.config(bg='#0A4D68')

frame = Frame(tk)
frame.pack(pady=10)

lb = Listbox(
    frame,
    
    width=80,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)


for item in todo:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    tk,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(tk)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add New Task',
    font=('times 14'),
    bg='#088395',
    padx=20,
    pady=10,
    fg= '#ffffff',
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#05BFDB',
    padx=20,
    pady=10,
    fg= '#ffffff',
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


tk.mainloop()