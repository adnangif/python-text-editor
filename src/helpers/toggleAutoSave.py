import tkinter as tk
from tkinter import filedialog,messagebox
import main

def toggleAutoSave(master: main.App):
    def inner_function(event=None):
        master.autoSave = not master.autoSave


    return inner_function