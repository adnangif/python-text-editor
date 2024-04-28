import pytest
from unittest.mock import MagicMock, patch
from tkinter import messagebox
import tkinter as tk

from countwords.countwords import GetCount
TEXT_BOX_START = '1.0'

main = __import__("main")
utils= __import__("utils")


empty_string = '\n'



def test_clear_empty_content():
    app = main.App()
    utils.Clear(app)()
    content = app.main_text_box.get(TEXT_BOX_START,tk.END)
    assert content == empty_string  

def test_clear_large_text():
    app = main.App()
    app.main_text_box.insert(TEXT_BOX_START, "i am\n a\n student and adsf;lkajsdfkcxvzcnv sdfxzcvdfgad dsfasdzx")
    utils.Clear(app)()
    content = app.main_text_box.get(TEXT_BOX_START,tk.END)
    assert content == empty_string