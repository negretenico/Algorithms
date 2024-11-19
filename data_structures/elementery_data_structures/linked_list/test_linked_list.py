import unittest
from data_structures.elementery_data_structures.linked_list.linked_list import LinkedList, Node

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        # Initialize an empty linked list before each test
        self.linked_list = LinkedList()

    def test_prepend(self):
        # Prepend nodes to the list
        self.linked_list.prepend(Node(10))
        self.linked_list.prepend(Node(5))
        self.linked_list.prepend(Node(15))

        # Check that the linked list order is as expected
        self.assertEqual(self.linked_list.to_list(), [15, 5, 10])

    def test_search(self):
        # Add nodes to the list
        self.linked_list.prepend(Node(10))
        self.linked_list.prepend(Node(5))
        self.linked_list.prepend(Node(15))

        # Search for existing and non-existing nodes
        self.assertIsNotNone(self.linked_list.search(10))
        self.assertIsNone(self.linked_list.search(20))

    def test_delete(self):
        # Add nodes to the list
        node1 = Node(10)
        node2 = Node(5)
        node3 = Node(15)
        self.linked_list.prepend(node1)
        self.linked_list.prepend(node2)
        self.linked_list.prepend(node3)

        # Delete the middle node and verify list integrity
        self.linked_list.delete(node2)
        self.assertEqual(self.linked_list.to_list(), [15, 10])

        # Delete the head node and verify
        self.linked_list.delete(node3)
        self.assertEqual(self.linked_list.to_list(), [10])

    # Helper method to convert linked list to a Python list for easier testing
    def to_list(self):
        current = self.linked_list.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values

# Run the test cases
if __name__ == '__main__':
    unittest.main()
