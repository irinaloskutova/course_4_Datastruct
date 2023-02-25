
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack:
    # instance_class = []
    def __init__(self, top=None):
        self.top = top

    def push(self, value) -> None:
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.top = new_node

    # def top(self):
    #     return Stack.instance_class.pop()

# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)
# print(n2.data)
# print(n1)
# print(n2.next_node)
#
stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack)
# # stack.push('data4')
# print(stack.top.data)
# print(stack.top.next_node.data)
# print(stack.top.next_node.next_node.data)
# print(stack.top.next_node.next_node.next_node)
# print(stack.top.next_node.next_node.next_node.data)

