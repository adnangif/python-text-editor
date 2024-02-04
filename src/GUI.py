import tkinter as tk
import tkinter.scrolledtext as tkst
import utils

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file_path: str = ""
        self.content: str = ""

        
        self.title("Text Editor")
        self.option_add("*Font",'aerial 13')

        self.geometry("700x500")

        self.menu_bar = tk.Menu(master=self)
        self.menu_item_File = tk.Menu(self.menu_bar,tearoff=0)
        self.menu_item_Edit = tk.Menu(self.menu_bar,tearoff=0)

        self.menu_item_File.add_command(label="Open",command=utils.Open(master=self))
        self.menu_item_File.add_command(label="Save As",command=utils.SaveAs(master=self))
        self.menu_item_File.add_command(label="Save",command=utils.Save(master=self))
        self.menu_item_File.add_command(label="Exit",command=utils.Exit(master=self))

        self.menu_item_Edit.add_command(label="Copy All",command=utils.CopyAll(master=self))
        self.menu_item_Edit.add_command(label="Paste",command=utils.Paste(master=self))
        self.menu_item_Edit.add_command(label="Clear",command=utils.Clear(master=self))
        
        self.menu_bar.add_cascade(label="File",menu=self.menu_item_File)
        self.menu_bar.add_cascade(label="Edit",menu=self.menu_item_Edit)

        self.config(menu=self.menu_bar)


        ## Text Box
        self.main_text_box = tkst.ScrolledText(master=self,undo=True)
        self.main_text_box.pack(padx=10,pady=10,expand='yes',fill='both')






if __name__ == '__main__':
    app = App()
    app.mainloop()


