class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyDict:
    def __init__(self, max_size=50):
        self.max_size = max_size
        self.size = 0
        self.elem = 0
        self.indx = 0
        self.elements = [None] * self.max_size

    def hash(self, key):
        return hash(key) % self.max_size

    def get(self, key):
        index = self.hash(key)
        element = self.elements[index]

        while element is not None\
                and element.key != key:
            element = element.next

        if element is None:
            return None
        else:
            return element.value

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        element = self.elements[index]

        if element is None:
            self.elements[index] = Element(key, value)
            return

        while element.next is not None:
            element = element.next

        element.next = Element(key, value)

    def remove(self, key):
        index = self.hash(key)
        element = self.elements[index]
        prev = None

        while element is not None and element.key != key:
            prev = element
            element = element.next

        if element is None:
            return None

        result = element.value

        if prev is None:
            self.elements[index] = element.next
        else:
            prev.next = prev.next.next

        self.size -= 1
        return result

    def size(self):
        return self.size

    def __next__(self):
        if self.elem is not None:
            current = self.elem
            self.elem = self.elem.next
            return current.key, current.value

        self.indx += 1
        if self.indx == self.max_size:
            raise StopIteration
        self.elem = self.elements[self.indx]

        return self.__next__()

    def __iter__(self):
        self.indx = 0
        self.elem = self.elements[0]
        return self

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __len__(self):
        return self.size
