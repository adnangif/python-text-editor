import tkinter as tk
from tkinter import filedialog,messagebox
import main
TEXT_BOX_START = '1.0'


def Clear(master):
    def inner_function(event=None):
        master.main_text_box.delete(TEXT_BOX_START,tk.END)
    
    return inner_function