import tkinter as tk
from tkinter import filedialog,messagebox
import main



def ReplaceAll(master: main.App):
    def inner_function(event=None):
    
      
        search_string = master.find_text_entry.get()
        new_string = master.replace_text_entry.get()

        if(search_string.strip() == ''):
            return
        if(new_string.strip() == ''):
            return
        content = master.main_text_box.get('1.0',tk.END)
        content = content.replace(search_string,new_string)
            
        master.main_text_box.delete("1.0", "end")

    
        master.main_text_box.insert("1.0", content)

    return inner_function;