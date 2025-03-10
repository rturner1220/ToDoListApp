import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

# Global task list (shared with main.py)
tasks = []
completed_tasks = []

def update_task_list(task_list):
    """
    Updates the task display in the GUI.
    :param task_list: Tkinter task list.
    """
    task_list.delete(0, "end")  # Clear the list
    for task in tasks:
        task_list.insert("end", task)


def add_task(task_entry, task_list):
    """
    Adds a task to the list after validating the input.
    :param task_entry: Tkinter entry field.
    :param task_list: Tkinter task list.
    """
    task = task_entry.get().strip()  # Remove leading/trailing spaces
    if not task:
        messagebox.showwarning("Warning", "Please enter a task!")
    elif any(char.isdigit() for char in task):  # Prevent numbers in tasks
        messagebox.showwarning("Warning", "Task should not contain numbers!")
    else:
        tasks.append(task)
        update_task_list(task_list)
        task_entry.delete(0, "end")

def delete_task(task_list):
    """
    Removes a selected task from the list.
    :param task_list: Tkinter task list.
    """
    try:
        selected_task_index = task_list.curselection()[0]
        del tasks[selected_task_index]
        update_task_list(task_list)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks(task_list):
    """
    Clears all tasks from the list.
    :param task_list: Tkinter task list.
    """
    tasks.clear()
    completed_tasks.clear() 
    update_task_list(task_list)

def mark_task_complete(task_list):
    """Marks a selected task as completed and moves it to the completed tasks list."""
    try:
        selected_task_index = task_list.curselection()[0]
        completed_tasks.append(tasks[selected_task_index])  # Move to completed list
        del tasks[selected_task_index]  # Remove from main list
        update_task_list(task_list)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def open_completed_tasks(root):
    """Opens a second window to display completed tasks."""
    second_window = tk.Toplevel(root)
    second_window.title("Completed Tasks")
    second_window.geometry("300x450")
    
      # Add Completed Task Icon at the Top
    try:
        img2 = Image.open("images/checkmark.png").convert("RGBA")
        img2 = img2.resize((30, 30))  
        img2 = ImageTk.PhotoImage(img2)

        img_label2 = tk.Label(second_window, image=img2, text="Task Completed", compound="top")
        img_label2.image = img2
        img_label2.pack(pady=10)

    except FileNotFoundError:
        img_label2 = tk.Label(second_window, text="Completed Task Icon Not Found", font=("Arial", 10, "bold"))
        img_label2.pack(pady=10)
        print("Error: Completed task icon not found.")

    
    completed_task_list = tk.Listbox(second_window, width=40, height=15)
    completed_task_list.pack(pady=10)

    # Populate completed tasks list
    for task in completed_tasks:
        completed_task_list.insert("end", task)

    close_button = tk.Button(second_window, text="Close", command=second_window.destroy)
    close_button.pack(pady=5)
