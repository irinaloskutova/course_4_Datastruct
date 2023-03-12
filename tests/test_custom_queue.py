import unittest

from custom_queue import Queue, Node

class TestQueue(unittest.TestCase):
    n1 = Node(1)
    a1 = Queue()

    def test_Node(self):
        self.assertEqual(self.n1.data, 1)
        self.assertEqual(self.n1.next_node, None)

    def test_Queue(self):
        self.assertEqual(self.a1.head, None)
        self.assertEqual(self.a1.tail, None)

    def test_enqueue(self):
        self.assertEqual(self.a1.head, None)

    def test_dequeue(self):
        self.assertEqual(self.a1.head, None)




