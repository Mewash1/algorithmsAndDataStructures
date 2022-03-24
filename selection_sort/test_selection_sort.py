from selection_sort import selection_sort


def test_selection_sort1():
    unsorted_array = [4, 3, 1, 5, 45]
    sorted_array = selection_sort(unsorted_array)
    assert sorted_array == [1, 3, 4, 5, 45]


def test_selection_sort_with_repetitions():
    unsorted_array = [4, 3, 1, 5, 45, 54, 2345, 1, 4, 5, 6]
    sorted_array = selection_sort(unsorted_array)
    assert sorted_array == [1, 1, 3, 4, 4, 5, 5, 6, 45, 54, 2345]


def test_negative_numbers():
    unsorted_array = [4, 3, 1, -5, 45, 54, 2345, -1, 4, 5, 6]
    sorted_array = selection_sort(unsorted_array)
    assert sorted_array == [-5, -1, 1, 3, 4, 4, 5, 6, 45, 54, 2345]

