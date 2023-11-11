import unittest
from DZ5 import binary_search


class BinarySearchTest(unittest.TestCase):
    def test_binary_search(self):
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        item = 5

        result = binary_search(sequence, item)
        self.assertEqual(result, 4)  # Ожидаемый результат: индекс числа 5 в списке sequence

        sequence = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
        item = 4

        result = binary_search(sequence, item)
        self.assertEqual(result, 3)  # Ожидаемый результат: первый индекс числа 4 в списке sequence

        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        item = 11

        result = binary_search(sequence, item)
        self.assertIsNone(result)  # Ожидаемый результат: None, так как число 11 отсутствует в списке sequence

if __name__ == '__main__':
    unittest.main()




