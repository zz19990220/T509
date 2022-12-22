import unittest
from Game import Game
from Human import Human
from Board import Board

class TestLogic(unittest.TestCase):

    def test_game_get_winner(self):
        player_o = Human('O')
        player_x = Human('X')
        game = Game (player_o,player_x)
        game.board.rows = [
            [player_x, None, player_o],
            [None, player_x, None],
            [None, player_o, player_x],
        ]
        self.assertEqual(game.get_winner(), player_x)

        game.board.rows = [
            [player_x, None, player_o],
            [None, player_o, None],
            [player_o, player_o, player_x],
        ]
        self.assertEqual(game.get_winner(), player_o)

        game.board.rows = [
            [player_x, player_o, player_x],
            [player_o, player_x, player_o],
            [player_o, player_x, player_o],
        ]
        self.assertEqual(game.get_winner(), None)

    def test_board_init(self):
        board = Board()
        self.assertEqual(len(board.rows), 3)
        for row in board.rows:
            for col in row:
                self.assertEqual(col, None)

    def test_game_swith_player(self):
        player_o = Human('O')
        player_x = Human('X')
        game = Game (player_o,player_x)

        self.assertEqual(player_o, game.swith_player())
        self.assertEqual(player_x, game.swith_player())

    def test_game_make_move(self):
        player_o = Human('O')
        player_fake = FakePlayer()
        game = Game (player_o,player_fake)

        game.make_move(player_fake)

        self.assertEqual(player_fake, game.board.rows[0][0])

class FakePlayer:
    def move(self, left_position):
        return 1

if __name__ == '__main__':
    unittest.main()
