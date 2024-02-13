import sys
import tkinter as tk
from tkinter import filedialog,messagebox
import GUI



def Exit(master: GUI.App):
    def inner_function(event=None):
        content = master.main_text_box.get('1.0',tk.END);
        
        if(content == '' and master.file_path == ''):
            sys.exit()
        
        save_before_exit: bool = messagebox.askyesno("Are you sure?", "Save Changes?")
        if(save_before_exit == False):
            sys.exit()

        

        if(master.file_path == ''):
            master.file_path = filedialog.asksaveasfilename(filetypes=[("txt files ",".txt")],defaultextension=".txt")

        
        with open(master.file_path,'w') as fw:
            fw.write(content)
        
        sys.exit()
    
    return inner_function;