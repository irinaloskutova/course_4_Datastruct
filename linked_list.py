class Node:
    """Класс Node хранит полезные данные (словарь с данными) и ссылку на следующий узел"""
    def __init__(self, data: dict, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс LinkedList хранит ссылку на начало связанного списка и на его конец,
    т.е. на первый и последний Node"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self, x):
        """Принимает данные (словарь) и добавляет узел
        с этими данными в начало связанного списка"""
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, x):
        """Принимает данные (словарь) и добавляет узел с
    этими данными в конец связанного списка"""
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
            ll_string += ' None'
            print(ll_string)

ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
# {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None