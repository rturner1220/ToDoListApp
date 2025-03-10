import tkinter as tk
from helpers import add_task, delete_task, clear_tasks, mark_task_complete, open_completed_tasks

from PIL import Image, ImageTk
import os

# Get the absolute path to images
image_path1 = os.path.abspath("images/notepad.png")
image_path2 = os.path.abspath("images/checkmark.png")

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x600")

# IMAGES - Task Icon in Main Window
try: 
    img = Image.open(image_path1).convert("RGBA")  # Ensure the image exists
    img = img.resize((30, 30))  
    img = ImageTk.PhotoImage(img)
    
    img_label = tk.Label(root, image=img, text="Task List", compound="top")  # Fixed "to" → "top"
    img_label.image = img  # Prevent garbage collection
    img_label.pack(pady=10)  # This places the icon at the top

except FileNotFoundError:
    img_label = tk.Label(root, text="Task List", font=("Arial", 10, "bold"))
    img_label.pack(pady=10)
    print(f"Error: {image_path1} not found.")
       
# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.insert(0, "Enter your task here...") 
task_entry.pack(pady=10)

# Remove placeholder when user clicks
def clear_placeholder(event):
    if task_entry.get() == "Enter your task here...":
        task_entry.delete(0, "end")

task_entry.bind("<FocusIn>", clear_placeholder) 

task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

# Create a frame to hold both buttons in the same row
button_frame = tk.Frame(root)
button_frame.pack(pady=10) 

# Add and Delete Buttons inside the frame using grid layout
add_button = tk.Button(button_frame, text="Add Task", command=lambda: add_task(task_entry, task_list),
                       bg="#4CAF50", fg="white", activebackground="#45a049", font=("Arial", 10, "bold"))
add_button.grid(row=0, column=0, padx=5)  # Place in the first column

delete_button = tk.Button(button_frame, text="Delete Task", command=lambda: delete_task(task_list),
                          bg="#f44336", fg="white", activebackground="#d32f2f", font=("Arial", 10, "bold"))
delete_button.grid(row=0, column=1, padx=5)  # Place in the second column

# Buttons using helper functions
mark_complete_button = tk.Button(root, text="Mark as Completed", command=lambda: mark_task_complete(task_list),
                                 bg="#FFC107", fg="black", activebackground="#FFA000", font=("Arial", 10, "bold"))
mark_complete_button.pack(pady=10)

completed_tasks_button = tk.Button(root, text="Open Completed Tasks", command=lambda: open_completed_tasks(root),
                                   bg="#2196F3", fg="white", activebackground="#1976D2", font=("Arial", 10, "bold"))
completed_tasks_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear All Tasks", command=lambda: clear_tasks(task_list),
                         bg="#9E9E9E", fg="white", activebackground="#757575", font=("Arial", 10, "bold"))
clear_button.pack(pady=10)


# IMAGES

# Function to add Completed Task Icon in the Completed Tasks Window
def completed_tasks(root):
    """Opens a second window to display completed tasks with an icon."""
    second_window = tk.Toplevel(root)
    second_window.geometry("300x400")

   # Add Completed Task Icon at the Top
    try:
        img2 = Image.open(image_path2).convert("RGBA")
        img2 = img2.resize((30, 30))  
        img2 = ImageTk.PhotoImage(img2)

        img_label2 = tk.Label(second_window, image=img2, text="Task Completed", compound="top")
        img_label2.image = img2
        img_label2.pack(pady=10)

    except FileNotFoundError:
        img_label2 = tk.Label(second_window, text="✔ Completed Task Icon Not Found", font=("Arial", 10, "bold"))
        img_label2.pack(pady=10)
        print(f"Error: {image_path2} not found.")

    # Title Label
    label = tk.Label(second_window, text="Completed Tasks", font=("Arial", 14))
    label.pack(pady=10)

    # Completed Task Listbox
    completed_task_list = tk.Listbox(second_window, width=40, height=15)
    completed_task_list.pack(pady=10)

    # Populate completed tasks list
    for task in completed_tasks:
        completed_task_list.insert("end", task)

    # Close Button
    close_button = tk.Button(second_window, text="Close", command=second_window.destroy)
    close_button.pack(pady=5)



# Run the application
root.mainloop()
