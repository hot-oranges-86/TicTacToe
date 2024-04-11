import tkinter as tk
from tile import Tile
from boards import MyMessageBox
from copy import deepcopy
import math

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

        for button in self.buttons:  # assigns methods for every button
            self.button_method_binder(button)

    # Board setup

    def place_buttons(self) -> None:
        '''Places Tiles in a grid.'''
        temp = 0
        for i in range(3):
            for j in range(3):
                self.buttons[temp].grid(column=i, row=j, padx=5, pady=5)
                temp += 1

    def reset(self) -> None:
        for button in self.buttons:
            button.stock_image()
            self.give_command(button)

    def button_method_binder(self, button) -> None:
        '''Binds merged methods for a button.'''
        button.tile_bind(lambda button: self.button_functions_merge(button))

    # methods

    def get_parent_frame(self, game_frame) -> None:
        '''Sets recived frame as a pranet frame.'''
        self.parent_frame = game_frame

    def check_for_win(self, button) -> bool:
        '''Checks for win.'''
        for way in WAYS_TO_WIN:
            # prevents form counting empty tiles
            if self.buttons.index(button) in way:
                if self.buttons[way[0]]['image'] == self.buttons[way[1]]['image'] and self.buttons[way[0]]['image'] == self.buttons[way[2]]['image'] and self.buttons[way[1]]['image'] == self.buttons[way[2]]['image']:
                    return True
        return False

    # TURN and MOVE controls

    def get_turn(self) -> bool:
        return TURN

    def move_reset(self) -> None:
        '''Sets global MOVE value to 0.'''
        global MOVE
        MOVE = 0

    def turn_change(self) -> None:
        global TURN
        TURN = not TURN

    def next_move(self) -> None:
        '''Increments global Move value.'''
        global MOVE
        MOVE += 1

    def after_click(self):
        self.next_move()
        self.turn_change()


class VsComputerBoard(Board):
    def __init__(self, parent, controller, icons):
        super(VsComputerBoard, self).__init__(parent, controller, icons)

    def button_functions_merge(self, button) -> None:
        '''Merges all functions into one that is easier to assign to lambda.'''
        Tile.left_click(button, TURN)
        self.after_click()
        self.after_move(button)

        self.max_player = 'O' if TURN == 'X' else 'X'
        self.winner = None

        best_move = self.computer_move(self.get_state(self), self.max_player)
        if best_move['position'] is not None:
            best_move = self.buttons[best_move['position']]

            Tile.left_click(best_move, TURN)
            self.after_click()
            self.after_move(best_move)

    def after_move(self, button) -> None:
        '''After move checks for win or draw.'''

        if MOVE > 4:
            if self.check_for_win(button):
                game_window = MyMessageBox(
                    self.controller, None, None, TURN)
                game_window.get_board(self)
                self.move_reset()

        if MOVE == 9:
            game_window = MyMessageBox(
                self.controller, 'black', 'DRAW', TURN)
            game_window.get_board(self)
            self.move_reset()

    def get_state(self, board) -> list[str]:
        '''Retuns list of X O or Empty, reporesends acutal board.'''
        state = []
        for button in board.buttons:
            if str(button['image']) == str(self.icons['X-Tile']):
                state.append('X')
            if str(button['image']) == str(self.icons['O-Tile']):
                state.append('O')
            if str(button['image']) == str(self.icons['emptyTile']):
                state.append('Empty')
        # print (state)
        return state

    def available_moves(self, state) -> list[int]:
        '''Return list of indexes of empty fields'''
        moves = []
        for index, move in enumerate(state):
            if move == 'Empty':
                moves.append(index)
        return moves

    def won_last_move(self, last, state) -> bool:
        '''Checks if last move was the winning move.'''
        for way in WAYS_TO_WIN:
            if last in way:  # prevents form counting empty tiles
                if state[way[0]] == state[way[1]] == state[way[2]] != 'Empty':
                    return True
        return False

    def computer_move(self, state, player) -> (dict[str, int]):
        '''minmaxes computer's next move'''
        other_player = 'O' if player == 'X' else 'X'

        if self.winner == other_player:
            return {'position': None, 'value': 1 * (len(self.available_moves(state)) + 1) if other_player == self.max_player else -1 * (
                len(self.available_moves(state)) + 1)}
        elif not self.available_moves(state):
            return {'position': None, 'value': 0}

        if player == self.max_player:
            # each value should maximize
            best = {'position': None, 'value': -math.inf}
        else:
            best = {'position': None, 'value': math.inf}

        for possible_move in self.available_moves(state):
            if state[possible_move] == 'Empty':

                state[possible_move] = player
                if self.won_last_move(possible_move, state):
                    self.winner = player

                score = self.computer_move(deepcopy(state), other_player)

                state[possible_move] = 'Empty'
                self.winner = None
                score['position'] = possible_move

                if player == self.max_player:
                    if score['value'] > best['value']:
                        best = score
                else:
                    if score['value'] < best['value']:
                        best = score

        return best
