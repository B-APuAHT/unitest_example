import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_empty(self):
        """Test swap_k with empty list"""
        actual = []
        a1.swap_k(actual, 0)
        expected = []
        self.assertEqual(actual, expected)

    def test_swap_k_smaller_evenLen_single(self):
        """Test swap_k with small even length list and single swap"""
        actual = [1, 2]
        a1.swap_k(actual, 1)
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_smaller_oddLen_single(self):
        """Test swap_k with small even length list and single swap"""
        actual = [1, 2, 3]
        a1.swap_k(actual, 1)
        expected = [3, 2, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_longer_evenLen_single(self):
        """Test swap_k with long even length list and single swap"""
        actual = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual, 1)
        expected = [6, 2, 3, 4, 5, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_longer_oddLen_single(self):
        """Test swap_k with long odd length list and single swap"""
        actual = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(actual, 1)
        expected = [7, 2, 3, 4, 5, 6, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_longer_evenLen_many(self):
        """Test swap_k with long even length list and many swaps"""
        actual = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual, 3)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_swap_k_longer_oddLen_many(self):
        """Test swap_k with long odd length list and many swaps"""
        actual = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(actual, 3)
        expected = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
