import tkinter as tk
from tkinter import filedialog,messagebox
import GUI
import os

def set_clipboard_text(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def CopyAll(master: GUI.App):
    def inner_function(event=None):
        content=master.main_text_box.get('1.0',tk.END)
        set_clipboard_text(content)
    
    return inner_function;