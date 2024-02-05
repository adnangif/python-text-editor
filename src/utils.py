import tkinter as tk
from tkinter import filedialog,messagebox
import GUI

def Open(master: GUI.App):
    def inner_function(event=None):
        master.file_path = filedialog.askopenfilename()

        if(master.file_path == ''):
            print("No file was selected!!")
            return
        
        with open(master.file_path) as fo:
            content = fo.read()
            master.main_text_box.delete('1.0',tk.END)
            master.main_text_box.insert(index=tk.END,chars=content)
            master.title(master.file_path)
            master.content = content
    return inner_function;

def SaveAs(master: GUI.App):
    def inner_function(event=None):
        pass;
    
    return inner_function;

def Save(master: GUI.App):
    def inner_function(event=None):
        pass;
    
    return inner_function;

def Exit(master: GUI.App):
    def inner_function(event=None):
        pass;
    
    return inner_function;

def CopyAll(master: GUI.App):
    def inner_function(event=None):
        pass;
    
    return inner_function;
def Paste(master: GUI.App):
    def inner_function(event=None):
        pass;
    
    return inner_function;

def Clear(master: GUI.App):
    def inner_function(event=None):
        pass;
    
    return inner_function;
    
    
if __name__ == "__main__":
    pass