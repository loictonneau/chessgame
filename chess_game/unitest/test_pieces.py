import unittest

from chess_game import pieces


class PiecesTestCase(unittest.TestCase):
    def test_create_pieces(self):
        result = pieces.Piece("pawn", "black", [0, 0])
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
