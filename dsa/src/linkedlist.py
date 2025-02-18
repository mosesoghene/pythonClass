class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data_type):
        self._type = data_type
        self.head = None
        self.size = 0

    def add(self, data) -> None:
        new_node: Node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current: Node = self.head
        while current.next is not None: current = current.next
        current.next = new_node
        self.size += 1

    def remove(self, index) -> Node:
        self.__validate_bounds(index)
        if index == 0: return self.remove_first()
        if index == self.size - 1 : self.remove_last()
        previous: Node = self.head
        for _ in range(index - 1): previous = previous.next
        previous.next = previous.next.next
        self.size -= 1

    def __validate_bounds(self, index):
        if index < 0 or index >= self.size: raise IndexError('Index out of bounds')

    def remove_first(self) -> Node:
        if self.head is None: raise IndexError('Cannot remove from an empty list')
        element: Node = self.head.data
        self.head = self.head.next
        self.size -= 1
        return element

    def remove_last(self) -> Node:
        if self.size <= 1: return self.remove_first()
        current: Node = self.head
        while current.next is not None: current = current.next
        element: Node = current.next.data
        current.next = None
        self.size -= 1
        return element

    def insert(self, data, index) -> None:
        self.__validate_bounds(index)
        if index == 0: self.prepend(data)
        elif index == self.size: self.add(data)
        else:
            new_node: Node = Node(data)
            previous: Node = self.head
            for _ in range(index - 1): previous = previous.next
            new_node.next = previous.next
            previous.next = new_node
            self.size += 1

    def prepend(self, data):
        self.__validate_data(data)
        new_node: Node = Node(data)
        self.head = new_node
        self.size += 1

    def __validate_data(self, data):
        if not isinstance(data, self._type): raise TypeError(f'Data must be of type "{self._type}"')

    def get(self, index):
        self.__validate_bounds(index)
        current: Node = self.head
        for _ in range(index - 1): current = current.next
        return current.data

    def clear(self) -> None:
        self.head = None
        self.size = 0

    def contains(self, data):
        self.__validate_data(data)
        current: Node = self.head
        while current.next is not None:
            if current.data == data: return True
            current = current.next

        return False

    def index(self, data) -> int:
        if self.size == 0: raise IndexError('Cannot find element on empty list')
        current: Node = self.head
        index: int = 0
        while current.next is not None:
            if current.data == data: return index
            current = current.next
            index += 1
