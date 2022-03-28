def bubble_sort(unsorted_list):
    partition = 1
    while partition < len(unsorted_list):
        for i in range(len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
        partition += 1
    return unsorted_list