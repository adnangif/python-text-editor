import tkinter as tk
from tkinter import filedialog,messagebox
import GUI

def toggleAutoSave(master: GUI.App):
    def inner_function(event=None):
        master.autoSave = master.autoSave


    return inner_function