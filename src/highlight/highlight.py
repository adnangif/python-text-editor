from math import e
import tkinter as tk
from tkinter import filedialog,messagebox

HIGHLIGHT_BOX='highlight'
HIGHLIGHT_BACKGROUND='yellow'
HIGHLIGHT_FOREGROUND='black'
HIGHLIGHT_FIRST_INDEX='sel.first'
HIGHLIGHT_LAST_INDEX='sel.last'



def Highlight(master):
    def inner_function(event=None):
        try:
            start_index = master.main_text_box.index(HIGHLIGHT_FIRST_INDEX)
            last_index = master.main_text_box.index(HIGHLIGHT_LAST_INDEX)
            master.main_text_box.tag_configure(HIGHLIGHT_BOX,HIGHLIGHT_BACKGROUND,HIGHLIGHT_FOREGROUND)
            master.main_text_box.tag_add(HIGHLIGHT_BOX,start_index,last_index)
        except:
            return
    return inner_function;