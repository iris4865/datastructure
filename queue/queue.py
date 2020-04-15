class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, data: object):
        new_node = Node(data)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    def get(self) -> object:
        data = self.head.data
        self.head = self.head.next

        self.size -= 1
        return data

    def peek(self) -> object:
        return self.head.data

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
    
    def __reversed__(self):
        return reversed([data for data in self])
