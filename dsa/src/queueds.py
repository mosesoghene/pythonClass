class Queue:
    def __init__(self, data_type, capacity: int):
        self._data_type = data_type
        self._capacity = capacity
        self._queue: data_type = []

    def size(self):
        return len(self._queue)

    def enqueue(self, element):
        if self.is_full(): raise ValueError("Stack is full")
        if self.__validate_element(element):
            self._queue.append(element)
            return None
        raise TypeError(f"Element must be of type {self._data_type}")

    def __validate_element(self, element):
        return isinstance(element, self._data_type)

    def is_full(self):
        return len(self._queue) == self._capacity

    def is_empty(self):
        return len(self._queue) == 0

    def dequeue(self):
        if self.is_empty(): raise IndexError("Stack is empty")
        element = self._queue[0]
        self._queue.remove(element)
        return element

    def peek(self):
        if self.is_empty(): raise IndexError("Stack is empty")
        return self._queue[0]



