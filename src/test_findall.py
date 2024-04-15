import tkinter as tk
from findall.findall import FindAll


main = __import__("main")
utils= __import__("utils")

   
def test_inner_function_no_match():
    app = main.App()
    inner_function = FindAll(app)
    
    app.find_text_entry.insert(tk.END, 'search_term')
    inner_function()

    # No tags should be applied if search term doesn't match
    assert app.main_text_box.tag_ranges('found') == ()


def test_inner_function_single_match():
    app = main.App()
    inner_function = FindAll(app)
    
    app.main_text_box.insert(tk.END, 'This is a search_term')
    app.find_text_entry.insert(tk.END, 'search_term')
    inner_function()

    # Verify that tag 'found' has been applied to the matched text
    assert app.main_text_box.tag_ranges('found') != ()