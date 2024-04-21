import tkinter as tk
import os
from open.open import openFile

main = __import__("main")
utils= __import__("utils")

def test_open_content_with_invalid_path():
    # Mocking the main_text_box and file_path for testing
    master = main.App()
    master.file_path = ""
    # Insert some test content into the text box
    test_content = "Test content\nLine 2\nLine 3"
    
    master.main_text_box.insert(tk.END, test_content)
    
    result = openFile(master)
    
    assert result == False

def test_open_content_with_valid_path():
    # Mocking the main_text_box and file_path for testing
    master = main.App()
    master.file_path = "testopen.txt"
    # Insert some test content into the text box
    test_content = "Test content\nLine 2\nLine 3"
    
    master.main_text_box.insert(tk.END, test_content)
    
    result = openFile(master)
    
    assert result == True
    
def test_open_content_text_box_has_correct_content():
    # Mocking the main_text_box and file_path for testing
    master = main.App()
    master.file_path = "testopen.txt"
    # Insert some test content into the text box
    test_content = "Test content\nLine 2\nLine 3"
    
    open_content = "this file is for test open\n"
    
    master.main_text_box.insert(tk.END, test_content)
    
    result = openFile(master)
    
    assert open_content == master.main_text_box.get('1.0',tk.END)
    