from pandas import array
from merge_sort import (
    merge, merge_sort
)


def test_merge():
    array1 = [1, 2, 4, 6]
    array2 = [2, 4, 6, 8]
    array = [1, 2, 2, 4, 4, 6, 6, 8]
    assert array == merge(array1, array2)