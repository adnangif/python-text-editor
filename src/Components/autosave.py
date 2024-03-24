import tkinter as tk
from tkinter import filedialog,messagebox
import GUI
from . import helpers



def AutoSave(master: GUI.App):
    def inner_function(event=None):
        try:
            if(master.autoSave == False): return
         
            if (master.file_path==''):
                print("No file path was given")
                return
            
            helpers.save_content(master)  
        except Exception as e:
          messagebox.showerror(message=str(e),title="Error Found")      
    return inner_function;