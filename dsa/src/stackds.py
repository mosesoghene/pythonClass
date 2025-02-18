class Stack:
    def __init__(self, data_type, capacity: int):
        self._data_type = data_type
        self._capacity = capacity
        self._stack: data_type = []

    def size(self):
        return len(self._stack)

    def push(self, element):
        if self.is_full(): raise ValueError("Stack is full")
        if self.__validate_element(element):
            self._stack.append(element)
            return None
        raise TypeError(f"Element must be of type {self._data_type}")

    def __validate_element(self, element):
        return isinstance(element, self._data_type)

    def is_full(self):
        return len(self._stack) == self._capacity

    def is_empty(self):
        return len(self._stack) == 0

    def pop(self):
        if self.is_empty(): raise IndexError("Stack is empty")
        element = self._stack[-1]
        self._stack.pop()
        return element

    def peek(self):
        if self.is_empty(): raise IndexError("Stack is empty")
        return self._stack[-1]
