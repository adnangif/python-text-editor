import tkinter as tk
from tkinter import filedialog,messagebox

TEXT_BOX_START = '1.0'
COUNT_WORD_MESSAGEbOX_TITLE='word count'
COUNT_WORD_BLANK_STRING=' '


def GetCount(master):
    content = master.main_text_box.get(TEXT_BOX_START,tk.END)   
    words = content.split(COUNT_WORD_BLANK_STRING)     
    total_words = len(words)
    if(len(content.strip()) == 0):
        total_words = 0
    return total_words


def CountWords(master):
    def inner_function(event=None):
        total_words = GetCount(master)        

        messagebox.askokcancel(COUNT_WORD_MESSAGEbOX_TITLE,message=f"Total number of words is: {total_words}")
    
    return inner_function