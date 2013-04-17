import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_null(self):
        """Test num_buses with 0 """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_min_for_1(self):
        """Test num_buses with minimum value to correspond with 1 bus """
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_value_equal_capacity(self):
        """Test num_buses with value that aliquot 50 """
        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_min_for_many(self):
        """Test num_buses with minimum value to correspond with many buses """
        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(actual, expected)

    def test_num_buses_max_for_many(self):
        """Test num_buses with maximum value to correspond with many buses """
        actual = a1.num_buses(149)
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
