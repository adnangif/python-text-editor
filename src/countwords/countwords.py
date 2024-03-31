import tkinter as tk
from tkinter import filedialog,messagebox

def GetCount(master):
    content = master.main_text_box.get('1.0',tk.END)   
    words = content.split(' ')     
    total_words = len(words)
    if(len(content.strip()) == 0):
        total_words = 0
    return total_words


def CountWords(master):
    def inner_function(event=None):
        total_words = GetCount(master)        

        messagebox.askokcancel(title='word count',message=f"Total number of words is: {total_words}")
    
    return inner_function