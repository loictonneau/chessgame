import unittest

from chess_game import pawn, pieces


class PawnTestCase(unittest.TestCase):
    def test_create_pawn(self):
        result = pawn.Pawn("pawn", "black", [0, 0])
        self.assertIsNotNone(result)
        self.assertIs(result.first_move, True)

    def test_get_available_move(self):
        board = []
        for each_rows in range(8):
            row = []
            for each_case in range(8):
                row.append(pieces.Piece(None, None, [each_case, each_rows]))
            board.append(row)
        board[4][4] = pawn.Pawn("pawn", "white", [4, 4])
        board[3][3] = pawn.Pawn("pawn", "black", [3, 3])
        board[3][5] = pawn.Pawn("pawn", "black", [3, 5])
        result = pawn.Pawn.get_available_move(board[4][4], board)
        self.assertListEqual(result, [[3, 4], [2, 4], [3, 3], [3, 5]])



if __name__ == '__main__':
    unittest.main()
