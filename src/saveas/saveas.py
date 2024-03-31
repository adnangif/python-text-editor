import tkinter as tk
from tkinter import filedialog,messagebox
import main
from helpers import helpers


def SaveAs(master):
    def inner_function(event=None):
        try:
            master.file_path=filedialog.asksaveasfilename(filetypes=[("txt files ",".txt")],defaultextension=".txt")
            helpers.save_content(master)

        except Exception as e:
            messagebox.showerror(message=str(e),title="Error Found")       
                





    return inner_function