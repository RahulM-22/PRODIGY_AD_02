import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")

# Define the listbox and scrollbar
listbox = tk.Listbox(root, height=15, width=50, font=("Arial", 14))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Attach the listbox to the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Define the entry widget to enter tasks
task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.pack(pady=10)

# Define functions for add, edit, delete tasks
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(tk.END, task)
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to edit.")

# Define buttons for the app
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Run the main loop
root.mainloop()
