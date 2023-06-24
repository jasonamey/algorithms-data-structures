class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        for i in range(len(array)):
            self.shiftUp(i)
        return array

    def siftDown(self):
        idx = 0
        if len(self.heap) == 1:
            return self.heap
        child = self._findChild(idx, self.heap)
        while child < len(self.heap) and self.heap[idx] > self.heap[child]:
            self._swap(idx, child, self.heap)
            idx = child
            child = self._findChild(idx, self.heap)
        return self.heap

    def shiftUp(self, idx):
        temp = idx
        parent = (temp - 1) // 2
        while temp != 0 and self.heap[temp] < self.heap[parent]:
            self._swap(temp, parent, self.heap)
            temp = parent
            parent = (temp - 1) // 2
        return self.heap

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def remove(self):
        item = self.peek()
        self._swap(0, len(self.heap) - 1, self.heap)
        self.heap.pop()
        self.siftDown()
        return item

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1)

    def __repr__(self):
        return str(self.heap)

    def _findChild(self, idx, arr):
        child = idx * 2 + 1
        if idx * 2 + 2 < len(arr):
            child = child if arr[child] < arr[idx * 2 + 2] else idx * 2 + 2
        return child

    def _swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


# mh = MinHeap([9, 1, 2, 4, 3])
# print(mh)
# print(mh.remove())
# mh.insert(5)
# mh.insert(1)
# print(mh)
