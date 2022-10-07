import unittest

from chess_game import knight


class KnightTestCase(unittest.TestCase):
    def test_create_knight(self):
        result = knight.Knight("knight", "black", [0, 0])
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
