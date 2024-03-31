import tkinter as tk
from tkinter import filedialog,messagebox


def toggleAutoSave(master):
    def inner_function(event=None):
        master.autoSave = not master.autoSave


    return inner_function