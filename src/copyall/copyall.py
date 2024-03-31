import tkinter as tk
from tkinter import filedialog,messagebox
import main
import os

def set_clipboard_text(text):
    command: str = 'echo ' + text.strip() + '| clip'

    command.replace('\n','')
    os.system(command)

def CopyAll(master: main.App):
    def inner_function(event=None):
        content=master.main_text_box.get('1.0',tk.END)
        set_clipboard_text(content)
    
    return inner_function;