import unittest
import app


class IncrementTest(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(app.increment(3), 4)
