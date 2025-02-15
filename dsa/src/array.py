class Array:
    def __init__(self, size):
        self.size = size
        self.data = []

    def add(self, element):
        if len(self.data) < self.size:
            self.data.append(element)
            return
        raise IndexError

    def remove(self, element):
        self.data.remove(element)

    def clear(self):
        self.data = []

    def get(self, index):
        return self.data[index]

    def index(self, element):
        return self.data.index(element)

    def contains(self, element):
        return element in self.data

    def sort(self):
        self.data.sort()

    def __len__(self):
        return self.size

    def values(self):
        return self.data
