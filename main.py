def swapPositions(list, pos1, pos2):   
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def bubble_sort(unsorted_list):
    list_size = len(unsorted_list)
    print(list_size)
    for i in range(list_size):
        for j in range (0, list_size - i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                swapPositions(unsorted_list, j, j+1)
    print(unsorted_list)

#bubble_sort([12,6,13,7,87])

def insertion_sort(unsorted_list):
    sorted_sub_list = []
    value_to_insert = 0
    pointer_position = 0
    for i in range(len(unsorted_list)):
        pointer_position = i
        value_to_insert = unsorted_list[i]
        while pointer_position > 0 and unsorted_list[pointer_position - 1] > value_to_insert:
            unsorted_list[pointer_position] = unsorted_list[pointer_position - 1]
            pointer_position = pointer_position - 1
        unsorted_list[pointer_position] = value_to_insert
    print(unsorted_list)

insertion_sort([12,6,13,7,87])