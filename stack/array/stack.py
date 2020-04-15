class Stack:
    def __init__(self):
        self.head = []

    def push(self, data: object):
        self.head.append(data)

    def pop(self) -> object:
        return self.head.pop()

    def peek(self) -> object:
        return self.head[-1]

    def is_empty(self) -> bool:
        return self.head == None

    def __len__(self):
        return len(self.head)

    def __iter__(self):
        return reversed(self.head)

    def __str__(self):
        return str([data for data in self])
