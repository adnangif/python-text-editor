import tkinter as tk
from tkinter import filedialog,messagebox
import main
from helpers import helpers

SAVE_BLANK_STRING=''

def Save(master):
    def inner_function(event=None):
        try:
           
            if (master.file_path==SAVE_BLANK_STRING):
                master.file_path=filedialog.asksaveasfilename(filetypes=[("txt files ",".txt")],defaultextension=".txt")
            helpers.save_content(master)  

            
        except Exception as e:
            messagebox.showerror(message=str(e),title="Error Found")




    return inner_function;

