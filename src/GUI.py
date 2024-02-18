import tkinter as tk
from tkinter import scrolledtext
import utils


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file_path: str = ""
        self.content: str = ""
        self.isSaved: bool = False;
        self.isEdited:bool = False;

        
        self.title("Text Editor")
        self.option_add("*Font",'aerial 13')

        self.geometry("700x500")

        self.menu_bar = tk.Menu(master=self)
        self.menu_item_File = tk.Menu(self.menu_bar,tearoff=0)
        self.menu_item_Edit = tk.Menu(self.menu_bar,tearoff=0)

        self.menu_bar.add_cascade(label="File",menu=self.menu_item_File)
        self.menu_bar.add_cascade(label="Edit",menu=self.menu_item_Edit)

        self.config(menu=self.menu_bar)

        

        ## Text Box
        self.main_text_box = scrolledtext.ScrolledText(master=self,undo=True)
        self.main_text_box.pack(padx=10,pady=10,expand='yes',fill='both')


        ## Button functionality
        self.menu_item_File.add_command(label="Open",
                                        command=utils.Open(master=self),
                                        accelerator="Ctrl+O".rjust(15),
                                        )

        self.menu_item_File.add_command(label="Save As",
                                        command=utils.SaveAs(master=self),
                                        accelerator="Ctrl+Shift+S".rjust(15),
                                        )

        self.menu_item_File.add_command(label="Save",
                                        command=utils.Save(master=self),
                                        accelerator="Ctrl+S".rjust(15),
                                        )

        self.menu_item_File.add_command(label="Exit",
                                        command=utils.Exit(master=self),
                                        accelerator="Ctrl+Shift+X".rjust(15),
                                        )

        self.menu_item_Edit.add_command(label="Copy All",
                                        command=utils.CopyAll(master=self),
                                        accelerator="Ctrl+Shift+C".rjust(15),
                                        )

        self.menu_item_Edit.add_command(label="Paste",
                                        command=utils.Paste(master=self),
                                        accelerator="Ctrl+Shift+V".rjust(15),
                                        )

        self.menu_item_Edit.add_command(label="Clear",
                                        command=utils.Clear(master=self),
                                        accelerator="Ctrl+Shift+D".rjust(15),
                                        )

        self.menu_item_Edit.add_command(label="Undo",
                                        command=self.main_text_box.edit_undo,
                                        accelerator="Ctrl+Z".rjust(15),
                                        )

        self.menu_item_Edit.add_command(label="Redo",
                                        command=self.main_text_box.edit_redo,
                                        accelerator="Ctrl+Y".rjust(15),
                                        )
        
        self.menu_item_Edit.add_command(label="Highlight",
                                        command=utils.Highlight(master=self),
                                        )


        
        ## Bindings
        self.bind_all('<Control-o>', utils.Open(master=self))
        self.bind_all('<Control-s>', utils.Save(master=self))
        self.bind_all('<Control-S>', utils.SaveAs(master=self))
        self.bind_all('<Control-X>', utils.Exit(master=self))
        self.wm_protocol("WM_DELETE_WINDOW", utils.Exit(master=self))






if __name__ == '__main__':
    app = App()
    app.mainloop()



