import tkinter as tk
from tkinter import messagebox
import os


FILENAME = "death_counter.txt"

def load_counter ():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return int(file.read)
            except ValueError:
                return 0
    return 0

def save_counter ():
    with open(FILENAME, "w") as file:
        file.write(str(counter))
        
def increase_counter ():
    global counter
    counter += 1
    label_counter.config(text=str(counter))
    save_counter(counter)

def reset_counter():
    global counter
    response = messagebox.askyesno("Reset the counter","Are you sure you want to reset the counter?")
    if response:
        counter = 0
        label_counter.config(text=str(counter))
        save_counter(counter)

root = tk.Tk()     
root.title("Death Counter - Sekiro") 

counter = charge_counter():
    
label_counter = tk.Label(root, text=str(counter),)
label_counter.pack(pady=20)
 
button_increase = tk.Button(root, text="Reset", command=reset_counter, font=("Helvetica",14))
button_increase.pack(pady=10)

    