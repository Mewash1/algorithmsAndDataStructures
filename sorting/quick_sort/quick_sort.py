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
    pivot_list = [pivot]
    return quick_sort(unsorted_list[0:pivot_index]) + pivot_list + quick_sort(unsorted_list[pivot_index+1:])
