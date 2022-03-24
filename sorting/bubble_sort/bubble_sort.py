def bubble_sort(unsorted_list):
    swap = True
    partition = 1
    while swap:
        swap = False
        for i in range(len(unsorted_list) - partition):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                swap = True
        partition += 1
        print(swap)
    return unsorted_list

def bubble_sort2(unsorted_list):
    swap = True
    partition = 1
    while swap:
        swap = False
        for i in range(len(unsorted_list) - partition):
            if unsorted_list[i] > unsorted_list[i + 1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp
                swap = True
        partition += 1
    return unsorted_list