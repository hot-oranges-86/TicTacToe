import tkinter as tk
from methods import set_size
from menus import MainMenu
from views import GameVsComputer


class GUI(tk.Tk):  # Main window

    '''Main window for the game.'''

    def __init__(self, *args) -> None:
        tk.Tk.__init__(self, *args)

        self.icons = get_icons()

        self.set_parameters()

        self.container = self.make_mainframe()

        self.frames = {}
        for frame in (MainMenu, GameVsComputer):
            self.create_frame(frame)

        self.raise_frame(MainMenu)

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

    # frame control

    def raise_frame(self, frame_name) -> None:
        frame = self.frames[frame_name]
        frame.tkraise()

    def update_frame(self, frame_name) -> None:
        frame = self.frames[frame_name]
        frame.update()

    def destroy_frame(self, frame_name) -> None:
        frame = self.frames[frame_name]
        frame.destroy()

    def create_frame(self, frame):
        temp_frame = frame(self.container, self, self.icons)
        self.frames[frame] = temp_frame
        temp_frame.grid(row=0, column=0, sticky='nsew')


def get_icons() -> dict:
    icons = {}

    icons['WindowIcon'] = tk.PhotoImage(file='./Images/TTT_Logo.png')

    icons['emptyTile'] = tk.PhotoImage(file='./Images/EmptyTile.png')

    icons['X-Tile'] = tk.PhotoImage(file='./Images/X-Tile.png')

    icons['O-Tile'] = tk.PhotoImage(file='./Images/O-Tile.png')

    return icons


if __name__ == "__main__":
    root = GUI()

    root.mainloop()
