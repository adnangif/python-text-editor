import tkinter as tk
from tkinter import filedialog,messagebox
TEXT_BOX_START = '1.0'



def ReplaceAll(master):
    def inner_function(event=None):
    
      
        search_string = master.find_text_entry.get()
        new_string = master.replace_text_entry.get()

        if(search_string.strip() == ''):
            return
        if(new_string.strip() == ''):
            return
        content = master.main_text_box.get(TEXT_BOX_START,tk.END)
        content = content.replace(search_string,new_string)
            
        master.main_text_box.delete(TEXT_BOX_START, "end")

    
        master.main_text_box.insert(TEXT_BOX_START, content)

    return inner_function;