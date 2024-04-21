import tkinter as tk
from helpers.helpers import save_content
import os

main = __import__("main")
utils= __import__("utils")


def test_save_content_file_created():
    # Mocking the main_text_box and file_path for testing
    master = main.App()
    master.file_path = "test_file1234.txt"
    # Insert some test content into the text box
    test_content = "Test content\nLine 2\nLine 3"
    master.main_text_box.insert(tk.END, test_content)
    
    save_content(master)
    
    assert os.path.exists(master.file_path) == True

    
def test_save_content():
    # Mocking the main_text_box and file_path for testing
    master = main.App()
    master.file_path = "test_file1234.txt"
    # Insert some test content into the text box
    test_content = "Test content\nLine 2\nLine 3"
    master.main_text_box.insert(tk.END, test_content)
    
    result = save_content(master)
    
    os.remove(master.file_path)
    
    assert result == True
    
    
def test_save_content_with_no_path():
    # Mocking the main_text_box and file_path for testing
    master = main.App()
    master.file_path = ""
    # Insert some test content into the text box
    test_content = "Test content\nLine 2\nLine 3"
    master.main_text_box.insert(tk.END, test_content)
    
    result = save_content(master)
    
    assert result == False
