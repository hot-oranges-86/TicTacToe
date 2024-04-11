import tkinter as tk
from boards import VsComputerBoard

FONT_MAIN = ('Digital-7', 40)
FONT_SUB = ('Digital-7', 30)
FONT_SUB_2 = ('Digital-7', 20)


class Game(tk.Frame):
    '''Base game class, add tiles in a subclass.'''

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

    def pass_self(self) -> None:
        '''Passes Game frame to Tiles in a list.'''
        self.tiles.get_parent_frame(self)


class GameVsComputer(Game):
    def __init__(self, parent, controller, icons):
        super(GameVsComputer, self).__init__(parent, controller, icons)

        self.tiles = VsComputerBoard(self, controller, icons)

        self.pass_self()

    def create_top_bar(self):
        self.diff_lbl = tk.Label(
            self.top_bar, text='VS Computer', fg='red', font=FONT_MAIN)
        self.diff_lbl.pack()
