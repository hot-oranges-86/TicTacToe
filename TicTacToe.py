import tkinter as tk
from methods import set_size


class GUI(tk.Tk):  # Main window

    '''Main window for the game.'''

    def __init__(self, *args) -> None:
        tk.Tk.__init__(self, *args)

        self.set_parameters()

        self.container = self.make_mainframe()

    def set_parameters(self) -> None:  # sets parameters of main window
        self.geometry(set_size(self, 500, 500))
        self.resizable(False, False)
        self.title('TicTacToe')
        self.iconphoto(False, self.icons['WindowIcon'])

    def make_mainframe(self) -> tk.Frame:  # makes containter for all the windows
        mainframe = tk.Frame(self)
        mainframe.pack(side='top', fill='both', expand=True)
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        return mainframe


if __name__ == "__main__":
    root = GUI()

    root.mainloop()
