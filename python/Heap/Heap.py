class Heap:
    def __init__(self):
        self.heap = [-1]

    def push(self, data):
        self.heap.append(data)

        idx = len(self.heap) - 1
        while idx > 1:
            if self.heap[idx] > self.heap[idx // 2]:
                break

            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx = idx // 2

    
    def pop(self):
        if len(self.heap) == 2:
            return self.heap.pop()

        idx = 1
        data = self.heap[idx]
        self.heap[idx] = self.heap.pop()

        child_idx = idx * 2
        while child_idx < len(self.heap):
            if child_idx+1 < len(self.heap) and self.heap[child_idx] < self.heap[child_idx+1]:
                child_idx += 1
            
            if self.heap[idx] <= self.heap[child_idx]:
                break
            
            self.heap[idx], self.heap[child_idx] = self.heap[child_idx], self.heap[idx]

        return data

    def __iter__(self):
        new_data = Heap()
        new_data.heap = self.heap[:]
        while len(new_data):
                    yield new_data.pop()

    def __len__(self) -> int:
        return len(self.heap) - 1

    def __str__(self) -> str:
        return str(self.heap[1:])