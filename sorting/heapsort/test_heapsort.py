import unittest
from sorting.heapsort import heapsort


class TestHeapsort(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(heapsort.heapsort([2, 3, 1]), [1, 2, 3])

    def test_case2(self):
        self.assertEqual(heapsort.heapsort([4, 1, 3, 2, 16, 9, 10, 14, 8, 7]), [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])

    def test_case3(self):
        self.assertEqual(heapsort.inbuilt_heap_sort([4, 1, 3, 2, 16, 9, 10, 14, 8, 7]), [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
    def test_case4(self):
        self.assertEqual(heapsort.inbuilt_heap_sort([2, 3, 1]), [1, 2, 3])
if __name__ == '__main__':
    unittest.main()