import tkinter as tk
from methods import set_size

FONT_MAIN = ('Digital-7', 40)
FONT_SUB = ('Digital-7', 30)
FONT_SUB_2 = ('Digital-7', 20)


class MyMessageBox(tk.Toplevel):

    def __init__(self, controller, color, text, turn, *args):
        tk.Toplevel.__init__(self, *args)

        self.turn = turn
        self.color = self.get_color(color)
        self.text = self.get_text(text)

        self.properties()

        self.controller = controller

        self.info = tk.Label(self, text=self.text,
                             fg=self.color, font=FONT_SUB).pack()

        self.play_again = tk.Button(self, text='PLAY AGAIN', font=FONT_SUB_2,
                                    command=self.command_btn_1).pack(side='left', padx=20)

        self.finish_game = tk.Button(
            self, text='QUIT', font=FONT_SUB_2, command=self.command_btn_2).pack(side='right', padx=20)

    def properties(self) -> None:
        self.title('Game Finished')
        self.resizable(False, False)
        self.overrideredirect(True)
        self.geometry(set_size(self, 350, 200))
        self['highlightbackground'] = self.color
        self['highlightthickness'] = 2

    def get_color(self, color):
        if color == None:
            color = 'blue' if self.turn else 'red'

        return color

    def get_text(self, text) -> str:
        if text == None:
            text = 'PLAYER' if self.turn else 'COMPUTER'
            text = text + ' WON'

        return text

    def get_board(self, board):
        self.board = board

    def command_btn_1(self):
        self.destroy()
        self.board.reset()

    def command_btn_2(self):
        self.destroy()
        self.controller.destroy()
