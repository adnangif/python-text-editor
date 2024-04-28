import tkinter as tk
from highlight.highlight import Highlight


main = __import__("main")
utils= __import__("utils") 
TEXT_BOX_START = '1.0'
TEXT_BOX_START2 = '1.4'
TEST_HIGHLIGHT_TEST='This is a test.'
TEST_HIGHLIGHT_TAG='sel'

def test_inner_function_highlight():
    app = main.App()
    inner_function = Highlight(app)


    app.main_text_box.insert(tk.END, TEST_HIGHLIGHT_TEST)

    # Select a portion of the text
    app.main_text_box.tag_add(TEST_HIGHLIGHT_TAG, TEXT_BOX_START , TEXT_BOX_START2)

    # Call inner_function to highlight the selected text
    inner_function()

    # Check if the selected text is highlighted
    tag_ranges = app.main_text_box.tag_ranges('highlight')
    assert tag_ranges != ()  # The 'highlight' tag should be applied

def test_inner_function_no_selection():
    app = main.App()
    inner_function = Highlight(app)

    # Insert some text into the text box
    app.main_text_box.insert(tk.END,TEST_HIGHLIGHT_TEST)

    # Call inner_function without any selection
    inner_function()

    # Check if there is no 'highlight' tag applied
    tag_ranges = app.main_text_box.tag_ranges('highlight')
    assert tag_ranges == () 
    