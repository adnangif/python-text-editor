import tkinter as tk
from tkinter import scrolledtext
import utils

MAIN_FONT='aerial 13'
TITLE="Text Editor"
FONT="*Font"
GEOMETRY="700x500"
NUM1=0 
NUM2=1
NUM3=2
NUM4=3
NUM5=8
NUM6=10
NUM7=15
MAIN_EMPTY_STRING=""



class App(tk.Tk):
    def basic_setups(self):
        self.title(TITLE)
        self.option_add(FONT,MAIN_FONT)
        self.geometry(GEOMETRY)

    def set_menu_bar(self):
        self.menu_bar = tk.Menu(master=self)
        self.menu_item_File = tk.Menu(self.menu_bar,tearoff=0)
        self.menu_item_Edit = tk.Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="File",menu=self.menu_item_File)
        self.menu_bar.add_cascade(label="Edit",menu=self.menu_item_Edit)
        self.config(menu=self.menu_bar)

    def set_find_all(self):
        self.find_frame = tk.Frame(master=self)
        self.find_frame.pack()

        self.find_text_label = tk.Label(master=self.find_frame,text='Search: ')
        self.find_text_entry = tk.Entry(master=self.find_frame)
        self.find_text_btn = tk.Button(master=self.find_frame,
                                        text="Find All Occurances",
                                        command=utils.FindAll(master=self)
                                        )

        self.find_text_label.grid(row=NUM1,column=NUM1,pady=NUM3)
        self.find_text_entry.grid(row=NUM1,column=NUM2,columnspan=NUM3,pady=NUM3)
        self.find_text_btn.grid(row=NUM1,column=NUM4,pady=NUM3,padx=NUM5) 
    
    def set_replace_all(self):
        self.replace_frame = tk.Frame(master=self)
        self.replace_frame.pack()

        self.replace_text_label = tk.Label(master=self.replace_frame,text='replace: ')
        self.replace_text_entry = tk.Entry(master=self.replace_frame)
        self.replace_text_btn = tk.Button(master=self.replace_frame,
                                        text="replace All Occurances",
                                        command=utils.ReplaceAll(master=self)
                                        )

        self.replace_text_label.grid(row=NUM1,column=NUM1,pady=NUM3)
        self.replace_text_entry.grid(row=NUM1,column=NUM2,columnspan=NUM3,pady=NUM3)
        self.replace_text_btn.grid(row=NUM1,column=NUM4,pady=NUM3,padx=NUM5)  

    def set_main_text_box(self):
        self.main_text_box = scrolledtext.ScrolledText(master=self,undo=True)
        self.main_text_box.pack(padx=NUM6,pady=NUM6,expand=True,fill='both')
    
    def set_btn_functionality(self):
        self.menu_item_File.add_command(label="Open",command=utils.Open(master=self),accelerator="Ctrl+O".rjust(NUM7),)
        self.menu_item_File.add_command(label="Save As", command=utils.SaveAs(master=self),accelerator="Ctrl+Shift+S".rjust(NUM7),)
        self.menu_item_File.add_command(label="Save",command=utils.Save(master=self), accelerator="Ctrl+S".rjust(NUM7),)
        self.menu_item_File.add_command(label="Exit",command=utils.Exit(master=self),accelerator="Ctrl+Shift+X".rjust(NUM7),)
        self.menu_item_Edit.add_command(label="Copy All",command=utils.CopyAll(master=self), accelerator="Ctrl+Shift+C".rjust(NUM7),)
        self.menu_item_Edit.add_command(label="Paste",command=utils.Paste(master=self),accelerator="Ctrl+Shift+V".rjust(NUM7), )
        self.menu_item_Edit.add_command(label="Clear", command=utils.Clear(master=self), accelerator="Ctrl+Shift+D".rjust(NUM7),  )
        self.menu_item_Edit.add_command(label="Undo", command=self.main_text_box.edit_undo,accelerator="Ctrl+Z".rjust(NUM7),)
        self.menu_item_Edit.add_command(label="Redo",command=self.main_text_box.edit_redo,accelerator="Ctrl+Y".rjust(NUM7), )
        self.menu_item_Edit.add_command(label="Highlight",command=utils.Highlight(master=self), )
        self.menu_item_Edit.add_command(label="Toggle Auto Save", command=utils.toggleAutoSave(master=self), )
        self.menu_item_Edit.add_command(label="Word count", command=utils.CountWords(master=self), )

    def set_bindings(self):
        self.bind_all('<Control-o>', utils.Open(master=self))
        self.bind_all('<Control-s>', utils.Save(master=self))
        self.bind_all('<Control-S>', utils.SaveAs(master=self))
        self.bind_all('<Control-X>', utils.Exit(master=self))
        self.bind_all('<Control-C>', utils.CopyAll(master=self))
        self.wm_protocol("WM_DELETE_WINDOW", utils.Exit(master=self))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file_path: str = MAIN_EMPTY_STRING
        self.content: str = MAIN_EMPTY_STRING
        self.isSaved: bool = False
        self.isEdited:bool = False
        self.autoSave:bool = False
        
        self.basic_setups()
        self.set_menu_bar()
        self.set_find_all()
        self.set_replace_all()
        self.set_main_text_box()
        self.set_btn_functionality()
        self.set_bindings()

        

    def auto_save_text_file(self):
        utils.AutoSave(master=self)()

        self.after(3000,self.auto_save_text_file)


if __name__ == '__main__':
    app = App()



    app.auto_save_text_file()
    app.mainloop()




