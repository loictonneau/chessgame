import unittest

from chess_game import pawn


class PawnTestCase(unittest.TestCase):
    def test_create_pawn(self):
        result = pawn.Pawn("pawn", "black", [0, 0])
        self.assertIsNotNone(result)
        self.assertIs(result.first_move, True)


if __name__ == '__main__':
    unittest.main()
