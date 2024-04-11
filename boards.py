import tkinter as tk
from tile import Tile

TURN = 0
'''checks if it's players turn'''
MOVE = 0
'''move counter'''

WAYS_TO_WIN = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
    (0, 4, 8), (2, 4, 6)  # diagonal
]
'''Ways to win a tictactoe game.'''


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

    def place_buttons(self) -> None:
        '''Places Tiles in a grid.'''
        temp = 0
        for i in range(3):
            for j in range(3):
                self.buttons[temp].grid(column=i, row=j, padx=5, pady=5)
                temp += 1

    def check_for_win(self, button) -> bool:
        '''Checks for win.'''
        for way in WAYS_TO_WIN:
            # prevents form counting empty tiles
            if self.buttons.index(button) in way:
                if self.buttons[way[0]]['image'] == self.buttons[way[1]]['image'] and self.buttons[way[0]]['image'] == self.buttons[way[2]]['image'] and self.buttons[way[1]]['image'] == self.buttons[way[2]]['image']:
                    return True
        return False


class VsComputerBoard(Board):
    def __init__(self, parent, controller, icons):
        super(VsComputerBoard, self).__init__(parent, controller, icons)
