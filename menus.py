import tkinter as tk
from views import GameVsComputer

FONT_MAIN = ('Digital-7', 40)
FONT_SUB = ('Digital-7', 30)
FONT_SUB_2 = ('Digital-7', 20)


class Menu(tk.Frame):

    def __init__(self, parent, controller, icons):
        tk.Frame.__init__(self, parent)

        self.grid(row=0, column=0)

        self.parent = parent
        self.controller = controller
        self.icons = icons

        self.directions = []  # list for frame names

        self.main_label = tk.Label(self, font=FONT_MAIN, fg='red')
        self.buttons = [tk.Button(self, font=FONT_SUB) for i in range(3)]

        self.in_place()

    def set_texts(self, main_text, buttons_text) -> None:
        '''set texts for each button'''

        self.main_label['text'] = main_text
        for index, button in enumerate(self.buttons):
            button['text'] = buttons_text[index]

    def navigate_to(self, index: int, direction: tk.Frame) -> None:
        '''Sets navigation to a button.'''
        self.buttons[index]['command'] = lambda: self.controller.raise_frame(
            direction)

    def edit_button_function(self, button_index, func):
        '''Change onclick for a given button.'''
        self.buttons[button_index].bind("<Button-1>", lambda _: func())

    def in_place(self):
        self.main_label.pack(anchor='n', pady=40)
        for button in self.buttons:
            button.pack(pady=10)


class MainMenu(Menu):
    def __init__(self, parent, controller, icons):
        super(MainMenu, self).__init__(parent, controller, icons)

        self.button_texts = ['PLAY', 'OPTIONS', 'QUIT']

        self.set_texts('TicTacToe', self.button_texts)

        self.navigate_to(0, GameVsComputer)

        self.edit_button_function(2, self.controller.destroy)

        self.buttons[1].destroy()  # remove when options implemented
        '''Options to be implemented.'''
