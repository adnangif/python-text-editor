import tkinter as tk
from tkinter import filedialog,messagebox




def FindAll(master):
    def inner_function(event=None):
        master.main_text_box.tag_configure('found',background='blue',foreground='white')
        master.main_text_box.tag_remove('found','1.0',tk.END)
        search_string = master.find_text_entry.get()

        if(search_string.strip() == ''):
            return
        start = "1.0"
        while True:
            start = master.main_text_box.search(search_string, start, stopindex=tk.END)
            if not start:
                break
            end = f"{start}+{len(search_string)}c"
            master.main_text_box.tag_add("found", start, end)
            start = end 
    return inner_function;