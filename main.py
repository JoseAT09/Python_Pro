import tkinter as tk
from tkinter import messagebox

def add_tarea():
    tarea = entry.get()
    if tarea:
        listbox.insert(tk.END, tarea)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no es valida.")

def remove_tarea():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_tarea)
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea primero")

def complete_tarea():
    try:
        selected_tarea = listbox.curselection()[0]
        listbox.itemconfig(selected_tarea, {'bg':'light gray'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea primero")

app = tk.Tk()
app.title("Lista de Tareas")

frame = tk.Frame(app)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

add_button = tk.Button(app, text="Agregar tarea", command=add_tarea)
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Eliminar tarea", command=remove_tarea)
remove_button.pack(pady=5)

complete_button = tk.Button(app, text="Completar tarea", command=complete_tarea)
complete_button.pack(pady=5)

app.mainloop()
