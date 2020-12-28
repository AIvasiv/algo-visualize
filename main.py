def swapPositions(list, pos1, pos2):   
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def bubble_sort(unsorted_list):
    list_size = len(unsorted_list)
    print(list_size)
    for j in range(0, list_size - 1):
        swapped = False
        for j in range (0, list_size - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                swapPositions(unsorted_list, j, j+1)
                swapped = True
    print(unsorted_list)

bubble_sort2([12,6,13,7,87])