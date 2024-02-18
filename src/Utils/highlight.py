import tkinter as tk
from tkinter import filedialog,messagebox
import GUI



def Highlight(master: GUI.App):
    def inner_function(event=None):
        start_index = master.main_text_box.index('sel.first')
        last_index = master.main_text_box.index('sel.last')
        master.main_text_box.tag_configure('highlight',background='yellow',foreground='black')
        master.main_text_box.tag_add('highlight',start_index,last_index)
    
    return inner_function;