import unittest

from data_structures.elementery_data_structures.stack.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        my_sttack = Stack(5)
        my_sttack.push(10)
        self.assertListEqual(my_sttack.stackk,[10])
    def test_pop(self):
        my_sttack = Stack(5)
        my_sttack.push(10)
        item = my_sttack.pop()
        self.assertEqual(item,10)
    def test_is_empty(self):
        my_sttack = Stack(5)
        self.assertTrue(my_sttack.is_empty())