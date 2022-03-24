from merge_sort.merge_sort import (
    merge, merge_sort
)


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