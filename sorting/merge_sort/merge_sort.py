
def merge(array1: list, array2: list) -> list:
    array = []
    length = len(array1)
    for i in range(length*2):
        if len(array1) != 0:
            el1 = array1[0]
        else:
            array += array2
            break

        if len(array2) != 0:
            el2 = array2[0]
        else:
            array += array1
            break

        if el1 <= el2:
            array.append(el1)
            array1.pop(0)
        else:
            array.append(el2)
            array2.pop(0)
    return array



def merge_sort(array: list) -> list:
    odd_offset = 1 if len(array) % 2 == 1 else 0
    q = len(array)//2
    if len(array) != 1:
        array1 = merge_sort(array[:q+odd_offset])
        array2 = merge_sort(array[q+odd_offset:])
        array = merge(array1, array2)
    return array



