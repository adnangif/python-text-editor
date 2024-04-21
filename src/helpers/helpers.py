from ast import Raise
import tkinter as tk
from tkinter import filedialog,messagebox




def save_content(master):
    try:
        
        content=master.main_text_box.get('1.0',tk.END)
        with open(master.file_path,'w') as fw:
            fw.write(content)
        
        return True
    except Exception as e:
        print(e)
        return False
