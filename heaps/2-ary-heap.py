from heap import AbstractHeap

class Heap(AbstractHeap):
    def __init__(self, data = None):
        self._heap = self._create_heap(data)

    def _create_heap(self, data):
        if data is None:
            return []
        last_index = (len(data)//2) - 1
        while last_index >= 0:
            self._heapify(data, last_index)
            last_index -= 1
        return data

    def _heapify(self, data, index):

        try:
            left_child = data[2 * index + 1]
        except IndexError:
            left_child = None
        
        try:
            right_child = data[2 * index + 2]
        except IndexError:
            right_child = None

        maximum = self._max_from_none(left_child, right_child)
        if maximum:
            if maximum[0] > data[index]:
                data[index], data[2 * index + maximum[1]] = data[2 * index + maximum[1]], data[index]
            self._heapify(data, 2 * index + maximum[1]) 
        
    def _max_from_none(self, left, right):
        if left and right:
            if left > right:
                return left, 1
            else:
                return right, 2
        elif left and not right:
            return left, 1
        elif not left and right:
            return right, 2
        else:
            return None

    def peek(self):
        if len(self._heap) != 0:
            return self._heap[0]
        else:
            return None

    def get_raw_data(self):
        return self._heap
    
    def push(self, value):
        self._heap.append(value)
        value_index = len(self._heap) - 1
        parent_index = (value_index - 1) // 2
        self._heapify(self._heap, parent_index)
    
    def pop(self):
        if len(self._heap) != 0:
            root = self._heap[0]
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            self._heap.pop()
            self._heapify(self._heap, 0)
            return root
        else:
            return None

    def __str__(self):
        pass 

heap = Heap([1,2])
print(heap.pop())

