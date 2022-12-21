# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import random
from logic import make_empty_board, get_winner, other_player


if __name__ == '__main__':
    with_bot = input('Playing with bot?  (Y/N)')
    board = make_empty_board()
    winner = None
    # human player is O, starts first
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

        #Input a move from the player.
        #bot player is X
        if(with_bot == 'Y' and player == 'X'):
            move = random.randrange(1, empty_count+1)
            print(f"Bot player - X, chosed {move} \n")
        else:
            move = input(f"Human player - {player}, choose a number from the board:\n>")
            move = int(move)

        # TODO: Update the board.
        empty_count = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == None:
                    empty_count += 1
                    if empty_count == move:
                        board[i][j] = player

        # Update who's turn it is.
        player = other_player(player)

        # TODO: Test if there's a winner
        winner = get_winner(board)

    print("Winner is:", winner)
