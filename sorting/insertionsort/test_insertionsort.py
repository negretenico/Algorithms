import unittest
from sorting.insertionsort import insertionsort


class TestQucksort(unittest.TestCase):

    def test_case_1(self):
        arr = [2, 3, 1]
        insertionsort.insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_case2(self):
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        insertionsort.insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
if __name__ == '__main__':
    unittest.main()