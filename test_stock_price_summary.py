import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty(self):
        """Test stock_price_summary with empty tuple"""
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_null(self):
        """Test stock_price_summary with null tuple"""
        actual = a1.stock_price_summary([0,0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_negative(self):
        """Test stock_price_summary with negative values"""
        actual = a1.stock_price_summary([-0.01, 0, -1, -2, 0])
        expected = (0, -3.01)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_positive(self):
        """Test stock_price_summary with positive values"""
        actual = a1.stock_price_summary([0.07, 0, 5, 0, 0])
        expected = (5.07, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_mixed(self):
        """Test stock_price_summary with mixed values"""
        actual = a1.stock_price_summary([0.07, -1, 5, -0.06, 0])
        expected = (5.07, -1.06)
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
