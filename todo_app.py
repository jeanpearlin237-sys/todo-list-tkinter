import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=20)

root.mainloop()