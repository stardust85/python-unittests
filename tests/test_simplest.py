import unittest
from app import simplest


class IncrementTest(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(simplest.increment(3), 4)
