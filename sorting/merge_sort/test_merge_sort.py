from merge_sort.merge_sort import (
    merge, merge_sort
)
from file_comprehension import turn_file_into_list

with open("pan-tadeusz.txt", 'r', encoding='utf-8') as file:
   pan_tadeusz = turn_file_into_list(file)


def test_merge_sort_words():
    unsorted_array = pan_tadeusz[:10]
    sorted_array = merge_sort(unsorted_array)
    assert sorted_array == ['Adam','Księga', 'Litwie', 'Mickiewicz', 'Pan',
    'Tadeusz', 'czyli', 'na', 'ostatni', 'zajazd']


def test_merge():
    array1 = [1, 2, 4, 6]
    array2 = [2, 4, 6, 8]
    array = [1, 2, 2, 4, 4, 6, 6, 8]
    assert array == merge(array1, array2)


def test_merge_sort_even():
    array3 = [2, 4, 6, 8, 4, 6, 2, 1]
    array = [1, 2, 2, 4, 4, 6, 6, 8]
    assert array == merge_sort(array3)


def test_merge_sort_odd():
    array3 = [2, 4, 6, 8, 4, 6, 2, 1, 5]
    array = [1, 2, 2, 4, 4, 5, 6, 6, 8]
    assert array == merge_sort(array3)


def test_merge_sort_odd_negative():
    array3 = [2, 4, 6, 8, 4, -6, 2, 1, 5, -2, -10]
    array = [-10, -6, -2, 1, 2, 2, 4, 4, 5, 6, 8]
    assert array == merge_sort(array3)


def test_merge_sort_benchmark_1000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:1000])


def test_merge_sort_benchmark_2000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:2000])


def test_merge_sort_benchmark_5000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:5000])


def test_merge_sort_benchmark_7000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:7000])


def test_merge_sort_benchmark_10000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:10000])