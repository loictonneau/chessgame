import unittest

from chess_game import pieces


class PiecesTestCase(unittest.TestCase):
    def test_create_pieces(self):
        result = pieces.Piece("pawn", "black", [0, 0])
        self.assertIsNotNone(result)

    def test_print_pieces(self):
        lowercase = ("p", "t", "c", "f", "d", "r")
        uppercase = ("P", "T", "C", "F", "D", "R")
        piece_type = ("pawn", "rook", "knight", "bishop", "queen", "king")
        color = ("black", "white")
        for color in color:
            for i in range(len(piece_type)):
                result = pieces.Piece(piece_type[i], color, [0, 0])
                if color == "black":
                    self.assertEqual(str(result), lowercase[i])
                if color == "white":
                    self.assertEqual(str(result), uppercase[i])
        result = pieces.Piece(None, None, [0, 0])
        self.assertEqual(str(result), "n")


if __name__ == '__main__':
    unittest.main()
