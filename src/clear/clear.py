import tkinter as tk
from tkinter import filedialog,messagebox
import main



def Clear(master):
    def inner_function(event=None):
        master.main_text_box.delete('1.0',tk.END)
    
    return inner_function