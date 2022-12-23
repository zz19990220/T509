class Board:
    def __init__(self):
        self.left_position_ctn = 9

        self.rows =  [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        board_str = ""
        self.left_position_ctn = 0

        for row in self.rows:
            for col in row:
                if col == None:
                    self.left_position_ctn += 1
                    board_str += str(self.left_position_ctn) + " "
                else:
                    board_str += col.label + " "
            board_str += "\n"

        return board_str