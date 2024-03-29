import tkinter as tk
from tkinter import filedialog,messagebox
import GUI


def CountWords(master: GUI.App):
    def inner_function(event=None):
        
        content = master.main_text_box.get('1.0',tk.END)
        
        words = content.split(' ')
        
        total_words = len(words)

        if(len(content.strip()) == 0):
            total_words = 0
        
        print(total_words)

        messagebox.askokcancel(title='word count',message=f"Total number of words is: {total_words}")
    
    return inner_function;