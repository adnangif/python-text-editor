import tkinter as tk
from tkinter import filedialog,messagebox




def save_content(master):
    content=master.main_text_box.get('1.0',tk.END)
    with open(master.file_path,'w') as fw:
        fw.write(content)
