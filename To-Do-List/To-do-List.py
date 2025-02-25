import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task.get("completed", False) else "❌"
        listbox_tasks.insert(tk.END, f"{status} {task['task']}")


def add_task():
    task = entry_task.get().strip()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks()
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")


def toggle_task_completion():
    try:
        selected_index = listbox_tasks.curselection()[0]    
        tasks[selected_index]["completed"] = not tasks[selected_index]["completed"]
        
        save_tasks()  
        update_task_list() 
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to toggle completion!")


def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        del tasks[selected_index]
        save_tasks()
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def delete_all_tasks():
    global tasks
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
        tasks = []
        save_tasks()
        update_task_list()


def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        new_task = entry_task.get().strip() 
        if new_task: 
            tasks[selected_index]["task"] = new_task
            save_tasks()  
            update_task_list()  
            entry_task.delete(0, tk.END)  
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to edit!")


def filter_tasks():
    query = entry_search.get().strip().lower()
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        if query in task["task"].lower():
            status = "✅" if task["completed"] else "❌"
            listbox_tasks.insert(tk.END, f"{status} {task['task']}")


root = tk.Tk()
root.title("To-Do List")
root.geometry("350x450")


entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=5)


btn_add = tk.Button(root, text="Add", command=add_task)
btn_add.pack(pady=2)

btn_complete = tk.Button(root, text="Complete", command=toggle_task_completion)
btn_complete.pack(pady=2)

btn_edit = tk.Button(root, text="Edit", command=edit_task)
btn_edit.pack(pady=2)

btn_delete = tk.Button(root, text="Delete", command=delete_task)
btn_delete.pack(pady=2)

btn_delete_all = tk.Button(root, text="Delete All", command=delete_all_tasks)
btn_delete_all.pack(pady=2)


entry_search = tk.Entry(root, width=30)
entry_search.pack(pady=5)
btn_search = tk.Button(root, text="Search", command=filter_tasks)
btn_search.pack(pady=2)


listbox_tasks = tk.Listbox(root, width=40, height=10)
listbox_tasks.pack(pady=5)


tasks = load_tasks()
update_task_list()


root.mainloop()
