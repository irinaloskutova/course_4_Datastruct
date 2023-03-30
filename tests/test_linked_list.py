import unittest

from linked_list import Node, LinkedList

class TestQueue(unittest.TestCase):
    n1 = Node({"key": "value"})
    l1 = LinkedList()
    l1.get_data_by_id([1, 2, 3])


    def test_Node(self):
        self.assertEqual(self.n1.data, {'key': 'value'})
        self.assertEqual(self.n1.next_node, None)

    def test_LinkedList(self):
        self.assertEqual(self.l1.head, None)
        self.assertEqual(self.l1.tail, None)

    def test_to_list(self):
        self.assertEqual(self.l1.to_list(), None)

    def test_get_data_by_id(self):
        self.assertEqual(self.l1.get_data_by_id('id'), 'Данные не являются словарем или в словаре нет id.')

