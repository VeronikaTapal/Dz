import unittest
from Dz43 import is_unique

class TestIsUnique(unittest.TestCase):

    def test_is_unique(self):
        self.assertFalse(is_unique("hello"))
        self.assertFalse(is_unique("hello world"))
        self.assertTrue(is_unique("12345"))
        self.assertFalse(is_unique("112233"))
        self.assertTrue(is_unique(""))
        self.assertTrue(is_unique("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(is_unique("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))

if __name__ == '__main__':
    unittest.main()