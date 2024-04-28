import tkinter as tk
from tkinter import filedialog,messagebox

import os
TEXT_BOX_START = '1.0'
def set_clipboard_text(text):
    command: str = 'echo ' + text.strip() + '| clip'

    command.replace('\n','')
    os.system(command)

def CopyAll(master):
    def inner_function(event=None):
        content=master.main_text_box.get(TEXT_BOX_START,tk.END)
        set_clipboard_text(content)
    
    return inner_function;