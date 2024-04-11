import tkinter as tk


class Board(tk.Frame):

    '''Container for tiles.'''

    def __init__(self, parent, controller, icons) -> None:
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        self.icons = icons

        # row 1 is for board row 0 is for top bar/score bar
        self.grid(row=1, column=0)
