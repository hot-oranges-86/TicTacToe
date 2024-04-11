import tkinter as tk
from tile import Tile


class Board(tk.Frame):

    '''Container for tiles.'''

    def __init__(self, parent, controller, icons) -> None:
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        self.icons = icons

        # row 1 is for board row 0 is for top bar/score bar
        self.grid(row=1, column=0)

        self.buttons = [Tile(self, icons) for i in range(9)]

        self.place_buttons()

    def place_buttons(self):
        temp = 0
        for i in range(3):
            for j in range(3):
                self.buttons[temp].grid(column=i, row=j, padx=5, pady=5)
                temp += 1
