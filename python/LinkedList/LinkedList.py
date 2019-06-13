class Node:
    def __init__(self, data: object):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data: object):
        new_node = Node(data)

        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    def insert(self, data: object, index: int) -> bool:
        if index > self.size:
            return False

        new_node = Node(data)
        if index == 0:
            if not self.head:
                self.head = new_node
                self.tail = self.head
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            prev_node = self._get_node_index(index - 1)
            next_node = prev_node.next

            if prev_node:
                prev_node.next = new_node
                new_node.prev = prev_node
            if next_node:
                new_node.next = next_node
                next_node.prev = new_node

        self.size += 1
        return True

    def delete_index(self, index: int) -> bool:
        node = self._get_node_index(index)
        if node:
            self._delete(node)
            return True
        return False

    def delete_data(self, data: object) -> bool:
        node = self._get_node_data(data)
        if node:
            self._delete(node)
            return True
        return False

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

    def get(self, index: int):
        return self._get_node_index(index).data

    def index(self, data: object) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def count(self) -> int:
        return self.size

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

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.head
        datas = []
        while current:
            datas.append(current.data)
            current = current.next
        return str(datas)
