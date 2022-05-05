from heap import AbstractHeap
import copy

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

    # def __str__(self):
    #     self._print_heap()

    def print_heap(self, data=None, padding=None, k=2, deep=None, first_element=True):
        data = copy.deepcopy(self._heap) if data is None else data
        deep = self._count_deep(k) if deep is None else deep
        if first_element:
            padding = self._give_padding(deep, k)
            padding = padding//2
            print(padding * ' ', end='')
            print(data[0])
            data.pop(0)
        else:
            padding //= 2
            print((padding)*' ', end='')
            count_sons = 0
            for i in range(k):
                count_sons += 1
                if len(data) != 0:
                    print(data[0], end='')
                    if count_sons % 2 != 0:
                        print((2 * padding + 1) * ' ', end='')
                    else:
                        print((2 * padding + 1) * ' ', end='')
                    data.pop(0)
                else:
                    print('')
                    return
            print('')
            print('')
            k *= 2
        self._print_heap(data, padding, k, deep, False)

    def _count_deep(self, k=2):
        data = copy.deepcopy(self._heap)
        deep = 1
        data.pop(0)

        while True:
            deep +=1
            for i in range(k):
                if len(data) != 0:
                    data.pop(0)
                else:
                    return deep
            k **= k



    def _give_padding(self, deep, k=2):
        deep -= 1
        padding = 0
        for i in range(deep):
            padding += k * 4
            k = k**2
        return padding

heap = Heap([1, 5, 4, 5, 8, 4, 3, 4, 3, 5, 4, 3, 2, 2, 5, 45, 3, 2, 4353, 3, 4, 4, 4, 5])
# print(heap.pop())
# str(heap)
heap._print_heap()
