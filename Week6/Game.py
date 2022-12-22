from Board import Board
import numpy as np

class Game:
    current_player = None; 

    def __init__(self, player_o, player_x):
        self.board = Board()

        self.player_o = player_o
        self.player_x = player_x
        
    def swith_player(self):
        if(Game.current_player == None 
            or Game.current_player == self.player_x):
            Game.current_player = self.player_o
        else:
           Game.current_player = self.player_x
           
        return Game.current_player
    
    def make_move(self, player):
        while True:
            move_to = player.move(self.board.left_position_ctn)
            if(move_to <= 0 or move_to > self.board.left_position_ctn):
                print (f"Incorret number, should between 1 and {self.board.left_position_ctn} choose again.")
            else:
                break
        
        empty_count = 0
        for i in range(len(self.board.rows)):
            for j in range(len(self.board.rows[i])):
                if self.board.rows[i][j] == None:
                    empty_count += 1
                    if empty_count == move_to:
                        self.board.rows[i][j] = player
                        return

    def get_winner(self):
        board = self.board.rows
        # Check rows
        for row in board:
            if row.count(self.player_x) == 3:
                return self.player_x
            if row.count(self.player_o) == 3:
                return self.player_o

        # Check columns
        transposed_board = np.array(board).T.tolist()

        for row in transposed_board:
            if row.count(self.player_x) == 3:
                return self.player_x
            if row.count(self.player_o) == 3:
                return self.player_o

        # Check diagonals
        if (board[0][0] == self.player_x and board[1][1] == self.player_x and board[2][2] == self.player_x) or (board[0][2] == self.player_x and board[1][1] == self.player_x and board[2][0] == self.player_x):
            return self.player_x

        if (board[0][0] == self.player_o and board[1][1] == self.player_o and board[2][2] == self.player_o) or (board[0][2] == self.player_o and board[1][1] == self.player_o and board[2][0] == self.player_o):
            return self.player_o

        return None