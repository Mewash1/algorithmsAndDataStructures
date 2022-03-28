def merge(array1: list, array2: list) -> list:
    array = []
    length_ar1 = len(array1)
    length_ar2 = len(array2)
    id_ar1 = 0
    id_ar2 = 0
    for i in range(length_ar1 + length_ar2):
        if len(array1[id_ar1:]) != 0:
            element_ar1 = array1[id_ar1:][0]
        else:
            array += array2[id_ar2:]
            break

        if len(array2[id_ar2:]) != 0:
            element_ar2 = array2[id_ar2:][0]
        else:
            array += array1[id_ar1:]
            break

        if element_ar1 <= element_ar2:
            array.append(element_ar1)
            id_ar1 += 1
        else:
            array.append(element_ar2)
            id_ar2 += 1
    return array


def merge_sort(array: list) -> list:
    odd_offset = 1 if len(array) % 2 == 1 else 0
    q = len(array)//2
    if len(array) != 1 and len(array) > 0:
        array1 = merge_sort(array[:q+odd_offset])
        array2 = merge_sort(array[q+odd_offset:])
        array = merge(array1, array2)
    return array
