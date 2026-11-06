import unittest


def tambah(a, b):
    return a + b


class TestCalculator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
