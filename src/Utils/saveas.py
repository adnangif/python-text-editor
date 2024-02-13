import tkinter as tk
from tkinter import filedialog,messagebox
import GUI



def SaveAs(master: GUI.App):
    def inner_function(event=None):
        content=master.main_text_box.get('1.0',tk.END)
        print(content)
        master.file_path=filedialog.asksaveasfilename(filetypes=[("txt files ",".txt")],defaultextension=".txt")
        print(master.file_path)   

        with open(master.file_path,'w') as fw:
            fw.write(content)





    return inner_function