class Node:
    def __init__(self, data: object):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data: object):
        def _insert(node: Node, data: object):
            if node:
                if data <= node.data:
                    node.left = _insert(node.left, data)
                else:
                    node.right = _insert(node.right, data)
            else:
                node = Node(data)
            return node

        self.root = _insert(self.root, data)
        self.size += 1

    def delete(self, data: object):
        def _delete(node: Node, data: object):
            if node and data == node.data:
                if node.left and node.right:
                    parent, child = node, node.right
                    while child.left:
                        parent, child = child, child.left
                    child.left = node.left
                    if parent != node:
                        parent.left = child.right
                        child.right = node.right
                    return child, True
                elif node.left or node.right:
                    return node.left or node.right, True
                else:
                    return None, True
            elif node:
                if data < node.data:
                    node.left, is_delete = _delete(node.left, data)
                else:
                    node.right, is_delete = _delete(node.right, data)
                return node, is_delete
            else:
                return None, False

        self.root, is_delete = _delete(self.root, data)
        if is_delete:
            self.size -= 1
        return is_delete

    def exist(self, data: object):
        def _exist(node: Node, data: object):
            if node:
                if data < node.data:
                    return _exist(node.left, data)
                elif data > node.data:
                    return _exist(node.right, data)
                else:
                    return True
            else:
                return False

        return _exist(self.root, data)

    def _inorder(self, node: Node):
        if node:
            return self._inorder(node.left) + [node.data] + self._inorder(node.right)
        else:
            return []

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in self._inorder(self.root):
            yield i

    def __str__(self):
        return str(self._inorder(self.root))