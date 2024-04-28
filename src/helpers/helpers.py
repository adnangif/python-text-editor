from ast import Raise
import tkinter as tk
from tkinter import filedialog,messagebox
TEXT_BOX_START = '1.0'
HELPERS_OPEN_STRING='W'



def save_content(master):
    try:
        
        content=master.main_text_box.get(TEXT_BOX_START,tk.END)
        with open(master.file_path,HELPERS_OPEN_STRING) as fw:
            fw.write(content)
        
        return True
    except Exception as e:
        print(e)
        return False
