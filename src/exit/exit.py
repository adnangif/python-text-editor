import sys
import tkinter as tk
from tkinter import filedialog,messagebox
TEXT_BOX_START = '1.0'
EXIT_BLANK_STRING =''
EXIT_MESSAGEBOX="Are you sure?"
EXIT_MESSAGEBOX2="Save Changes?"




def Exit(master):
    def inner_function(event=None):
        content = master.main_text_box.get(TEXT_BOX_START,tk.END);
        
        if(content == EXIT_BLANK_STRING and master.file_path == EXIT_BLANK_STRING):
            sys.exit()
        
        save_before_exit: bool = messagebox.askyesno(EXIT_MESSAGEBOX, EXIT_MESSAGEBOX2)
        if(save_before_exit == False):
            sys.exit()

        

        if(master.file_path == EXIT_BLANK_STRING):
            master.file_path = filedialog.asksaveasfilename(filetypes=[("txt files ",".txt")],defaultextension=".txt")

        
        with open(master.file_path,'w') as fw:
            fw.write(content)
        
        sys.exit()
    
    return inner_function;