def quick_sort(unsorted_list):
    if len(unsorted_list) == 1 or len(unsorted_list) == 0:
        return unsorted_list
    pivot = unsorted_list[-1]
    pivot_index = 0
    for i in range(len(unsorted_list) - 1):
        if unsorted_list[i] < pivot:
            unsorted_list[i], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[i]
            pivot_index += 1
    unsorted_list[-1], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[-1]
    if len(unsorted_list) == 2:
        return unsorted_list
    left, pivot_list, right = gen_left_pivot_right(unsorted_list, pivot, pivot_index)
    return quick_sort(left) + pivot_list + quick_sort(right)


def gen_left_pivot_right(partitioned_list, pivot, pivot_index):
    left, pivot_list, right = [], [pivot], []
    for element in partitioned_list[0:pivot_index]:
        if element != pivot:
            left.append(element)
        else:
            pivot_list.append(pivot)
    for element in partitioned_list[pivot_index+1:]:
        if element != pivot:
            right.append(element)
        else:
            pivot_list.append(pivot)
    return left, pivot_list, right
