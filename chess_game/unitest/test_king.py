import unittest

from chess_game import king


class KingTestCase(unittest.TestCase):
    def test_create_king(self):
        result = king.King("king", "black", [0, 0])
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
