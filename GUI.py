import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        self.mainloop()


#class BNT(GUI):
    #def buttons(self):



GUI('Kalorie app', (600, 600))