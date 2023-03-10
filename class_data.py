
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:

    def __init__(self, top=None):
        self.top = top
        # self.instance_class = []
    def push(self, value) -> None:
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        removed_node = self.top
        self.top = self.top.next_node
        return removed_node.data


# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)
# print(n2.data)
# print(n1)
# print(n2.next_node)
#
# stack = Stack()
# stack.push('data1')
# stack.push('data2')
# stack.push('data3')
# print(stack.top.data)
# print(stack.top.next_node.data)
# print(stack.top.next_node.next_node.data)
# print(stack.top.next_node.next_node.next_node)
# print(stack.top.next_node.next_node.next_node.data)

stack = Stack()
stack.push('data1')
data = stack.pop()

# стэк стал пустой
print(stack.top)
# None

# pop() удаляет элемент и возвращает данные удаленного элемента
print(data)
# 'data1'


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
# 'data1'

# данные удаленного элемента
print(data)
# 'data2'
