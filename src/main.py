import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.title("Text Editor")
        self.option_add("*Font",'aerial 13')

        self.geometry("700x500")

        self.menu_bar = tk.Menu(master=self)
        self.menu_item_File = tk.Menu(self.menu_bar,tearoff=0)
        self.menu_item_Edit = tk.Menu(self.menu_bar,tearoff=0)

        self.menu_item_File.add_command(label="Open")
        self.menu_item_File.add_command(label="Save As")
        self.menu_item_File.add_command(label="Save")
        self.menu_item_File.add_command(label="Exit")

        self.menu_item_Edit.add_command(label="Copy All")
        self.menu_item_Edit.add_command(label="Cut")
        self.menu_item_Edit.add_command(label="Paste")
        
        self.menu_bar.add_cascade(label="File",menu=self.menu_item_File)
        self.menu_bar.add_cascade(label="Edit",menu=self.menu_item_Edit)

        self.config(menu=self.menu_bar)


        ## Text Box
        self.main_text_box = ctk.CTkTextbox(master=self)
        self.main_text_box.pack(padx=10,pady=10,expand='yes',fill='both')





if __name__ == '__main__':
    app = App()
    app.mainloop()



