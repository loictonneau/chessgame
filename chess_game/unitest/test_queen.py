import unittest

from chess_game import queen


class QueenTestCase(unittest.TestCase):
    def test_create_queen(self):
        result = queen.Queen("queen", "black", [0, 0])
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
