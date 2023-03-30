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

    def to_list(self):
        '''to_list() - возвращает список с данными, содержащимися в односвязном списке LinkedList'''
        ll_list = []
        node = self.head
        if node is None:
            return None
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, value):
        """get_data_by_id() - возвращает первый найденный в LinkedList словарь с ключом id,
        значение которого равно переданному в метод значению. """
        ll_list = self.to_list()
        try:
            for item in ll_list:
                if item['id'] == value:
                    return item
        except:
            print("Данные не являются словарем или в словаре нет id.")
            return "Данные не являются словарем или в словаре нет id."


if __name__ == '__main__':
    # работа блока try/except
    ll = LinkedList()
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end('idusername')
    # ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    user_data = ll.get_data_by_id(2)
    # Данные не являются словарем или в словаре нет id.
    # Данные не являются словарем или в словаре нет id.
    print(user_data)
    # {'id': 2, 'username': 'mosh_s'}