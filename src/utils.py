import tkinter as tk
from tkinter import filedialog

def fileOpen():
    filepath: str = filedialog.askopenfilename();

    print(filepath)

    


if __name__ == "__main__":
    pass