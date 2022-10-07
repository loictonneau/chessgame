import unittest

from chess_game import bishop


class BishopTestCase(unittest.TestCase):
    def test_create_bishop(self):
        result = bishop.Bishop("bishop", "black", [0, 0])
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
