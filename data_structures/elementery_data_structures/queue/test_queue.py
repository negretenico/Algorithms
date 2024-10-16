import unittest
from data_structures.elementery_data_structures.queue.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        my_queue = Queue()
        my_queue.enqueue(10)
        my_queue.enqueue(5)
        my_queue.enqueue(15)
        self.assertListEqual(my_queue.get_queue(),[10,5,15])
    def test_deuque(self):
        my_queue = Queue()
        my_queue.enqueue(10)
        my_queue.enqueue(5)
        my_queue.enqueue(15)
        self.assertListEqual(my_queue.get_queue(),[5,15])
