import pytest
from unittest.mock import MagicMock, patch
from tkinter import messagebox

from countwords.countwords import GetCount


main = __import__("main")
utils= __import__("utils")
TEXT_BOX_START = '1.0'





def test_count_words_empty_content():
    app = main.App()
    word_count = GetCount(app)
    assert word_count == 0

def test_count_words_with_new_line():
    app = main.App()
    app.main_text_box.insert(TEXT_BOX_START, "i am\n a\n student")
    word_count = GetCount(app)
    assert word_count == 4

