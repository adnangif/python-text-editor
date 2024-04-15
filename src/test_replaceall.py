import tkinter as tk
from replaceall.replaceall import ReplaceAll

main = __import__("main")
utils= __import__("utils")

def test_inner_function_empty_search_string():
    app = main.App()
    inner_function = ReplaceAll(app)
    
    app.find_text_entry.insert(tk.END, '')
    app.replace_text_entry.insert(tk.END, 'replacement')
    inner_function()

    # No replacement should happen if search string is empty
    assert app.main_text_box.get('1.0', 'end') == '\n'


def test_inner_function_replace():
    app = main.App()
    inner_function = ReplaceAll(app)
    
    app.main_text_box.insert(tk.END, 'This is a search term')
    app.find_text_entry.insert(tk.END, 'search')
    app.replace_text_entry.insert(tk.END, 'replacement')
    inner_function()

    # Verify that search term is replaced with replacement
    assert app.main_text_box.get('1.0', 'end') == 'This is a replacement term\n\n'

def test_inner_function_empty_replace_string():
    app = main.App()
    inner_function = ReplaceAll(app)
    
    app.find_text_entry.insert(tk.END, 'search')
    app.replace_text_entry.insert(tk.END, '')
    inner_function()

    # No replacement should happen if replace string is empty
    assert app.main_text_box.get('1.0', 'end') == '\n'
