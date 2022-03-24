from bubble_sort import bubble_sort, bubble_sort2


def test_1(benchmark):
    benchmark(bubble_sort, [3,5,1,9,6,2]) == [1,2,3,5,6,9]

def test_2(benchmark):
    benchmark(bubble_sort2, [3,5,1,9,6,2]) == [1,2,3,5,6,9]