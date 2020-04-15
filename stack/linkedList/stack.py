class Node:
    def __init__(self, data: object):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data: object):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return

    def pop(self) -> object:
        data = self.peek()
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self) -> object:
        return self.head.data

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        return str([data for data in self])
