class MySet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def add(self, element):
        if element not in self.data: return None

        if len(self.data) < self.capacity:
            self.data.append(element)
            return None
        raise IndexError("Size is full")

    def remove(self, element):
        self.data.remove(element)

    def clear(self):
        self.data = []

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index is out of range")

    def index(self, element):
        return self.data.index(element)

    def contains(self, element):
        return element in self.data

    def sort(self):
        self.data.sort()

    def __len__(self):
        return self.capacity

    def size(self):
        return len(self.data)

    def values(self):
        return self.data
