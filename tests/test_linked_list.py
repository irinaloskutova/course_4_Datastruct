import unittest

from linked_list import Node, LinkedList

class TestQueue(unittest.TestCase):
    n1 = Node({"key": "value"})
    l1 = LinkedList()

    def test_Node(self):
        self.assertEqual(self.n1.data, {'key': 'value'})
        self.assertEqual(self.n1.next_node, None)

    def test_LinkedList(self):
        self.assertEqual(self.l1.head, None)
        self.assertEqual(self.l1.tail, None)

