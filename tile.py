import tkinter as tk


class Tile(tk.Button):

    '''Button widget with some styling and basic methods.'''

    def __init__(self, parent, icons) -> None:
        tk.Button.__init__(self, parent)
        self.icons = icons
        self.tile_look()

    def tile_look(self) -> None:
        '''Basic button look.'''
        self['relief'] = 'flat'
        self['bd'] = 0
        self['image'] = self.icons['emptyTile']

    def default_image(self) -> None:
        '''Sets buttons image to default image'''
        self['image'] = self.icons['emptyTile']

    def tile_bind(self, func) -> None:
        '''Binds function for a button.'''
        self.bind("<Button-1>", lambda _: func(self))

    def left_click(self, turn) -> None:
        '''Change button image on click.'''

        if turn:
            self['image'] = self.icons['X-Tile']
        else:
            self['image'] = self.icons['O-Tile']

        # stops image change if you cick multiple times
        self.bind("<Button-1>", lambda _: "break")
