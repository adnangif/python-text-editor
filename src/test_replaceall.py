import tkinter as tk
from replaceall.replaceall import ReplaceAll

main = __import__("main")
utils= __import__("utils")
TEXT_BOX_START = '1.0'
TEST_REPLACEALL_BLANK_STRING=''
TEST_REPLACEMENT='replacement'
TEST_END='end'
TEST_REPLACEMENT_SEARCH= 'search'
TEST_REPLACEMENT_SEARCHTERM='This is a search term'
TEST_REPLACEMENT_TERM='This is a replacement term\n\n'
EMPTY_STRING='\n'


def test_inner_function_empty_search_string():
    app = main.App()
    inner_function = ReplaceAll(app)
    
    app.find_text_entry.insert(tk.END,TEST_REPLACEALL_BLANK_STRING )
    app.replace_text_entry.insert(tk.END, TEST_REPLACEMENT)
    inner_function()

    # No replacement should happen if search string is empty
    assert app.main_text_box.get(TEXT_BOX_START, TEST_END) == EMPTY_STRING


def test_inner_function_replace():
    app = main.App()
    inner_function = ReplaceAll(app)
    
    app.main_text_box.insert(tk.END, TEST_REPLACEMENT_SEARCHTERM)
    app.find_text_entry.insert(tk.END, TEST_REPLACEMENT_SEARCH)
    app.replace_text_entry.insert(tk.END, TEST_REPLACEMENT)
    inner_function()

    # Verify that search term is replaced with replacement
    assert app.main_text_box.get(TEXT_BOX_START, TEST_END) == TEST_REPLACEMENT_TERM

def test_inner_function_empty_replace_string():
    app = main.App()
    inner_function = ReplaceAll(app)
    
    app.find_text_entry.insert(tk.END, TEST_REPLACEMENT_SEARCH)
    app.replace_text_entry.insert(tk.END, TEST_REPLACEALL_BLANK_STRING)
    inner_function()

    # No replacement should happen if replace string is empty
    assert app.main_text_box.get(TEXT_BOX_START, TEST_END) == EMPTY_STRING
