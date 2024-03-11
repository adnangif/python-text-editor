import tkinter as tk
from tkinter import filedialog,messagebox
import GUI



def AutoSave(master: GUI.App):
    def inner_function(event=None):
        if(master.autoSave == False): return
        content=master.main_text_box.get('1.0',tk.END)
        # print(content)
        if (master.file_path==''):
            print("No file path was given")
            return
        print(master.file_path)   

        with open(master.file_path,'w') as fw:
            fw.write(content) 
    return inner_function;