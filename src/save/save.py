import tkinter as tk
from tkinter import filedialog,messagebox
import GUI
from helpers import helpers

def Save(master: GUI.App):
    def inner_function(event=None):
        try:
           
            if (master.file_path==''):
                master.file_path=filedialog.asksaveasfilename(filetypes=[("txt files ",".txt")],defaultextension=".txt")
            helpers.save_content(master)  

            
        except Exception as e:
            messagebox.showerror(message=str(e),title="Error Found")




    return inner_function;

