from selection_sort.selection_sort import selection_sort
from file_comprehension import turn_file_into_list


with open("pan-tadeusz.txt", 'r', encoding='utf-8') as file:
    pan_tadeusz = turn_file_into_list(file)


def test_selection_sort_words():
    unsorted_array = pan_tadeusz[:10]
    sorted_array = selection_sort(unsorted_array)
    assert sorted_array == ['Adam', 'Księga', 'Litwie', 'Mickiewicz', 'Pan',
                            'Tadeusz', 'czyli', 'na', 'ostatni', 'zajazd']


def test_selection_sort_with_repetitions():
    unsorted_array = [4, 3, 1, 5, 45, 54, 2345, 1, 4, 5, 6]
    sorted_array = selection_sort(unsorted_array)
    assert sorted_array == [1, 1, 3, 4, 4, 5, 5, 6, 45, 54, 2345]


def test_negative_numbers():
    unsorted_array = [4, 3, 1, -5, 45, 54, 2345, -1, 4, 5, 6]
    sorted_array = selection_sort(unsorted_array)
    assert sorted_array == [-5, -1, 1, 3, 4, 4, 5, 6, 45, 54, 2345]


def test_selection_sort_benchmark_1000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:1000])


def test_selection_sort_benchmark_2000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:2000])


def test_selection_sort_benchmark_5000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:5000])


def test_selection_sort_benchmark_7000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:7000])


def test_selection_sort_benchmark_10000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:10000])
