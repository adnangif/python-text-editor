import tkinter as tk
from helpers.toggleAutoSave import toggleAutoSave

main = __import__("main")
utils= __import__("utils")


def test_toggleAutoSave_initial_state():
    # Test toggling autoSave from initial state (False)
    master = main.App()
    master.autoSave = False
    
    toggle_function = toggleAutoSave(master)
    toggle_function()
    
    assert master.autoSave == True
    

def test_toggleAutoSave_from_true_to_false():
    # Test toggling autoSave from True to False
    master = main.App()
    
    master.autoSave = True
    
    toggle_function = toggleAutoSave(master)
    toggle_function()
    
    assert master.autoSave == False

def test_toggleAutoSave_from_false_to_true():
    # Test toggling autoSave from False to True
    master = main.App()
    
    master.autoSave = False
    
    toggle_function = toggleAutoSave(master)
    toggle_function()
    
    assert master.autoSave == True
    
    