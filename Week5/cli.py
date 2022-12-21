# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'O'

    while winner == None:
        # TODO: Show the board to the user.
        board_str = ""
        empty_count = 0

        for row in board:
            for ele in row:
                if ele == None:
                    empty_count += 1
                    board_str += str(empty_count) + " "
                else:
                    board_str += ele + " "
            board_str += "\n"

        print(board_str)

        # TODO: Input a move from the player.
        move = input('Choose a number from the board:\n> ')
        move = int(move)

        # TODO: Update the board.
        empty_count = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == None:
                    empty_count += 1
                    if empty_count == move:
                        board[i][j] = player

        # TODO: Update who's turn it is.
        player = other_player(player)

        # TODO: Test if there's a winner
        winner = get_winner(board)

    print("Winner is:", winner)
