

def selection_sort(array: list) -> list:
    for id, second_element in enumerate(array):
        minimum_element = array[id]
        for element in array[id:]:
            if minimum_element > element:
                minimum_element = element
        id2 = array[id:].index(minimum_element) + id
        array[id] = minimum_element
        array[id2] = second_element
    return array
