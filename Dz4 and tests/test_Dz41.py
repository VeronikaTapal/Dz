import unittest
from Dz41 import rotate_list


class TestRotateList(unittest.TestCase):
    def test_rotate_list(self):
        elements = ['1', '2', '3', '4', '5']
        k = 3
        expected_result = ['3', '4', '5', '1', '2']
        self.assertEqual(rotate_list(elements, k), expected_result)

    def test_custom_rotate_list(self):
        elements = ['1', '2', '3', '4', '5']
        k = 3
        expected_result = ['3', '4', '5', '1', '2']

        for j in range(k):
            element = elements.pop()
            elements.insert(0, element)

        self.assertEqual(elements, expected_result)


if __name__ == '__main__':
    unittest.main()
