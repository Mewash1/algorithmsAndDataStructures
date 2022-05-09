from heap import AbstractHeap
import copy


class Heap(AbstractHeap):
    '''
    Class representing a d-ary heap. d = sons_quantity and must be given while creating the heap.
    If d is not given, then the heap will be a 2-ary heap.
    '''
    def __init__(self, sons_quantity = 2, data = None):
        if sons_quantity < 2:
            raise ValueError("heap must be at least 2-ary")
        self._sons_quantity = sons_quantity
        self._heap = self._create_heap(data)

    def _create_heap(self, data):
        if data is None:
            return []
        last_index = (len(data) - 2) // self._sons_quantity
        while last_index >= 0:
            self._heapify(data, last_index)
            last_index -= 1
        return data

    def _heapify(self, data, index, push=False):
        children = []
        for i in range(self._sons_quantity):
            try:
                child = data[self._sons_quantity * index + (i + 1)]
            except IndexError:
                child = None
            children.append(child)

        maximum = self._max_from_none(children)
        if maximum[0]:
            if maximum[0] > data[index]:
                data[index], data[self._sons_quantity * index + maximum[1]] = data[self._sons_quantity * index + maximum[1]], data[index]
            if not push:
                self._heapify(data, self._sons_quantity * index + maximum[1])
            elif index != 0:
                self._heapify(data, (index - 1) // self._sons_quantity)

    def _max_from_none(self, children):
        max_index, max_child = None, None
        for index, child in enumerate(children):
            if child is not None:
                if max_child is None or child > max_child:
                    max_child = child
                    max_index = index
        max_index = max_index + 1 if max_index is not None else None
        return max_child, max_index

    def peek(self):
        if len(self._heap) != 0:
            return self._heap[0]
        else:
            return None

    def get_raw_data(self):
        return self._heap

    def push(self, value):
        self._heap.append(value)
        if len(self._heap) != 1:
            value_index = len(self._heap) - 1
            parent_index = (value_index - 1) // self._sons_quantity
            self._heapify(self._heap, parent_index, True)

    def pop(self):
        if len(self._heap) != 0:
            root = self._heap[0]
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            self._heap.pop()
            self._heapify(self._heap, 0)
            return root
        else:
            return None

    def print_heap(self, data=None, padding=None, k=None, first_element=True):
        data = copy.deepcopy(self._heap) if data is None else data
        sons_quanity = self._sons_quantity
        k = sons_quanity if k is None else k
        deep = self._count_deep()

        padding = self._give_padding(deep) if padding is None else padding

        if first_element:
            print(padding * ' ', end='')
            print(data[0])
            data.pop(0)
        else:
            padding = padding // sons_quanity
            print((padding)*' ', end='')
            sons_count = 0
            for i in range(k):
                sons_count += 1
                if len(data) != 0:
                    print(data[0], end='')
                    print((2 * padding - 1) * ' ', end='')
                    data.pop(0)
                else:
                    print('')
                    return
            print('')
            print('')
            k *= sons_quanity
        self.print_heap(data, padding, k, False)

    def _count_deep(self):
        data = copy.deepcopy(self._heap)
        sons_in_a_row = self._sons_quantity
        sons_quanity = self._sons_quantity
        deep = 1
        data.pop(0)
        while True:
            deep += 1
            for i in range(sons_in_a_row):
                if len(data) != 0:
                    data.pop(0)
                else:
                    return deep
            sons_in_a_row *= sons_quanity

    def _give_padding(self, deep):
        deep -= 1
        padding = 0
        padding_multiplier = self._sons_quantity
        for i in range(deep):
            padding_multiplier *= 2
            padding += padding_multiplier
        padding = self._give_divisible_padding(padding)

        return padding

    def _give_divisible_padding(self, padding):
        sons_quantity = self._sons_quantity
        elemnets = []
        element = padding
        while element != 0:
            element = element // sons_quantity
            elemnets.append(element)

        new_padding = sons_quantity ** (len(elemnets) - 1)
        if new_padding == padding:
            return new_padding
        else:
            return new_padding * sons_quantity
