import tkinter as tk

FONT_MAIN = ('Digital-7', 40)
FONT_SUB = ('Digital-7', 30)
FONT_SUB_2 = ('Digital-7', 20)


class Game(tk.Frame):
    def __init__(self, parent, controller, icons):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.icons = icons

        self.center_board()

        self.top_bar = tk.Frame(self)
        self.top_bar.grid(row=0, column=0, sticky='new')

        self.create_top_bar()

    def center_board(self) -> None:
        '''Centers Tiles in the middle and topbar on top.'''

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_top_bar(self) -> None:
        '''Abstract method.'''
        raise NotImplementedError("Abstract method")
