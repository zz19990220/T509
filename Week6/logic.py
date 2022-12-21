# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import numpy as np


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    [
        [None, None, None],
        ['X', 'X', 'X'],
        [None, None, None],
    ]

    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'X'
        if row.count('O') == 3:
            return 'O'

    # Check columns
    transposed_board = np.array(board).T.tolist()

    for row in transposed_board:
        if row.count('X') == 3:
            return 'X'
        if row.count('O') == 3:
            return 'O'

    # Check diagonals
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return 'X'

    if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return 'O'

    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'O':
        return 'X'
    else:
        return 'O'
