import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

        board = [
            ['X', None, 'O'],
            [None, 'O', None],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), None)

    def test_make_empty_board(self):
        self.assertEqual(len(logic.make_empty_board()), 3)

        empty_board = logic.make_empty_board()

        for row in empty_board:
            for ele in row:
                self.assertEqual(ele, None)

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')


if __name__ == '__main__':
    unittest.main()
