class Node:
    def __init__(self, data: object):
        self.data = data
        self.prev = None
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

    def append(self, data: object):
        new_node = Node(data)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    def appendleft(self, data: object):
        new_node = Node(data)

        if self.head:
            self.head.next = new_node
            new_node.next = self.head
        else:
            self.tail = new_node

        self.head = new_node
        self.size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def count(self) -> int:
        return self.size

    def index(self, data) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def insert(self, data: object, index: int):
        if index == 0:
            self.appendleft(data)
        elif index == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            prev_node = self._get_node_index(index - 1)
            next_node = prev_node.next

            if prev_node:
                prev_node.next = new_node
                new_node.prev = prev_node
            if next_node:
                new_node.next = next_node
                next_node.prev = new_node
                self.size += 1

    def pop(self) -> object:
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        return data

    def popleft(self) -> object:
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def remove(self, data):
        node = self._get_node_data(data)
        if node:
            self._delete(node)
            return True
        return False

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def rotate(self, n):
        while n:
            if n > 0:
                self._rotate_right()
                n -= 1
            else:
                self._rotate_left()
                n += 1

    def _rotate_left(self):
        head = self.head.next
        head.prev = None
        node = self.head
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.head = head

    def _rotate_right(self):
        tail = self.tail.prev
        tail.next = None
        node = self.tail
        node.prev = None
        node.next = self.head
        self.head = node
        self.tail = tail

    def _delete(self, node: Node):
        if node.prev and node.next:  # center
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.next:  # head
            self.head = node.next
            self.head.prev = None
        else:  # tail
            self.tail = node.prev
            self.tail.next = None

        self.size -= 1

    def _get_node_index(self, index: int) -> Node:
        if index >= self.size:
            return None

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def _get_node_data(self, data: object) -> Node:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        current = self.head
        datas = []
        while current:
            datas.append(current.data)
            current = current.next
        return str(datas)
