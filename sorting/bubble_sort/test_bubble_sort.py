from bubble_sort.bubble_sort import bubble_sort, bubble_sort2
from file_comprehension import turn_file_into_list

with open("pan-tadeusz.txt", 'r', encoding='utf-8') as file:
   pan_tadeusz = turn_file_into_list(file)


# def test_1(benchmark):
#     benchmark(bubble_sort, [3,5,1,9,6,2]) == [1,2,3,5,6,9]

# def test_2(benchmark):
#     benchmark(bubble_sort2, [3,5,1,9,6,2]) == [1,2,3,5,6,9]


def test_bubble_sort_benchmark_1000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:1000])


def test_bubble_sort_benchmark_2000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:2000])


def test_bubble_sort_benchmark_5000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:5000])


def test_bubble_sort_benchmark_700(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:7000])

def test_bubble_sort_benchmark_10000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:10000])