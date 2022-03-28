def selection_sort(array: list) -> list:
    for id, second_element in enumerate(array):
        minimum_element = second_element
        id_min = id
        for id2, element in enumerate(array[id:]):
            if minimum_element > element:
                minimum_element = element
                id_min = id2 + id
        array[id] = minimum_element
        array[id_min] = second_element
    return array
