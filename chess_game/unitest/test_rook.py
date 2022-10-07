import unittest

from chess_game import rook


class RookTestCase(unittest.TestCase):
    def test_create_rook(self):
        result = rook.Rook("pawn", "black", [0, 0])
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
