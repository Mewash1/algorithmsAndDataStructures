from .d_ary_heap import Heap


def test_create_empty_heap():
    heap = Heap()
    assert heap.peek() is None
    assert heap.get_raw_data() == []
    assert heap.pop() is None

def test_create_2_ary_heap():
    heap = Heap(2, [1,2,3,4,5,6,7,8,9,10])
    assert heap.get_raw_data() == [10,9,7,8,5,6,3,1,4,2]
    i = 10
    while heap.peek():
        assert heap.peek() == i
        heap.pop()
        i -= 1
    assert heap.pop() is None
    assert heap.peek() is None

def test_push_2_ary_heap():
    heap = Heap(2, [1,2,3,4,5])
    heap.push(10)
    assert heap.get_raw_data() == [10,4,5,1,2,3]
    heap.push(6)
    assert heap.get_raw_data() == [10,4,6,1,2,3,5]
    heap.push(7)
    assert heap.get_raw_data() == [10,7,6,4,2,3,5,1]

def test_create_3_ary_heap():
    heap = Heap(3, [1,2,3,4,5,6,7,8,9,10])
    assert heap.get_raw_data() == [10,7,9,4,5,6,2,8,1,3]
    i = 10
    while heap.peek():
        assert heap.peek() == i
        heap.pop()
        i -= 1
    assert heap.pop() is None
    assert heap.peek() is None

def test_push_3_ary_heap():
    heap = Heap(3, [1,2,3,4,5])
    heap.push(10)
    assert heap.get_raw_data() == [10,5,3,4,1,2]
    heap.push(6)
    assert heap.get_raw_data() == [10,6,3,4,1,2,5]
    heap.push(7)
    assert heap.get_raw_data() == [10,6,7,4,1,2,5,3]

def test_create_4_ary_heap():
    heap = Heap(4, [1,2,3,4,5,6,7,8,9,10])
    assert heap.get_raw_data() == [10,9,3,4,5,6,7,8,2,1]
    i = 10
    while heap.peek():
        assert heap.peek() == i
        heap.pop()
        i -= 1
    assert heap.pop() is None
    assert heap.peek() is None

def test_push_4_ary_heap():
    heap = Heap(4, [1,2,3,4,5])
    heap.push(10)
    assert heap.get_raw_data() == [10,5,3,4,1,2]
    heap.push(6)
    assert heap.get_raw_data() == [10,6,3,4,1,2,5]
    heap.push(7)
    assert heap.get_raw_data() == [10,7,3,4,1,2,5,6]

def test_count_deep():
    heap = Heap(2, [1, 2, 3, 4, 5, 6, 7, 5])
    deep = heap._count_deep()
    assert deep == 4
    heap2 = Heap(3, [1, 2, 4, 5, 5, 3, 1, 5, 5])
    deep2 = heap2._count_deep()
    assert deep2 == 3
    heap3 = Heap(4,[1, 2, 3, 4, 5, 6, 7, 5])
    deep3 = heap3._count_deep()
    assert deep3 == 3

def test_print_tree():
    print('\n\nHeap 2-ary\n')
    heap = Heap(2, [1, 2, 3, 4, 5, 6, 7, 5, 8])
    heap.print_heap()
    print('\n\nHeap 3-ary\n')
    heap2 = Heap(3, [1, 2, 4, 5, 5, 3, 1, 5, 5, 6, 8, 8])
    heap2.print_heap()
    print('\n\nHeap 3-ary\n')
    heap3 = Heap(4,[1, 2, 3, 4, 5, 6, 7, 5, 4, 5, 6, 7, 8])
    print('\n\n\n')
    heap3.print_heap()
