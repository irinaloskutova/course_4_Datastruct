import unittest

from class_data import Node, Stack


class Test(unittest.TestCase):
    n1 = Node(5, None)
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    def test_Node(self):
        self.assertEqual(Test.n1.data, 5)
        self.assertEqual(Test.n1.next_node, None)

    def test_Stack(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
