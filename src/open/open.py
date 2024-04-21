import tkinter as tk
from tkinter import filedialog,messagebox


def openFile(master):
    try:
        with open(master.file_path) as fo:
            content = fo.read()
            master.main_text_box.delete('1.0',tk.END)
            master.main_text_box.insert(index=tk.END,chars=content)
            master.title(master.file_path) 
            master.content = content
            
        return True
    except Exception as e:
        print(e)
        return False

def Open(master):
    def inner_function(event=None):
        master.file_path = filedialog.askopenfilename()


        openFile(master)
        
        return master.content
    return inner_function