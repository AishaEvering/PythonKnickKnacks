import unittest
import guessingGame


class TestGame(unittest.TestCase):
    def test_get_range_when_guess_is_lower(self):
        """checking if a lower guess within in close range is correct"""
        expected = 2
        result = guessingGame.get_range(3, 5)
        self.assertEqual(result, expected)

    def test_get_range_when_guess_is_higher(self):
        """checking if a higher guess within in close range is correct"""
        expected = 2
        result = guessingGame.get_range(5, 3)
        self.assertEqual(result, expected)

    def test_get_range_when_guess_is_the_same(self):
        """checking if a same guess within in close range is correct"""
        expected = 0
        result = guessingGame.get_range(5, 5)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
