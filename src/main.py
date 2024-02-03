import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("system")

ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.title("Text Editor")

        self.geometry("500x500")

        

if __name__ == '__main__':
    app = App()
    
    app.mainloop()

