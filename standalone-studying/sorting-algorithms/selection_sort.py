import random

def selection_sort_v1(unodered_list):
    """
        my implementation of a selection sort algorithm

        - creates a new array instead of swapping the elements
    """

    # sums the cost to run the algorithm
    cost = 0

    ordered_list = []
    len_list = len(unodered_list)
    len_list_original = len_list

    for i in xrange(len_list):
        cost = cost + 1

        smallest_index = find_smallest_index(unodered_list, len_list)
        cost = cost + len_list

        smallest_item = unodered_list.pop(smallest_index)
        ordered_list.append(smallest_item)
        len_list = len_list - 1

    # print "*** selection_sort_v1***"
    # print "running time ~=", cost
    # print "N:", len(ordered_list)

    return ordered_list

def selection_sort_v2(alist):

    """
        implementation of a selection sort taken from: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html

        - swaps items
    """

    cost = 0
    for fillslot in range(len(alist)-1,0,-1):
        cost = cost + 1
        positionOfMax=0
        for location in range(1,fillslot+1):
            cost = cost + 1
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        cost = cost + 1
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

    # print "*** selection_sort_v2***"
    # print "running time ~=", cost
    # print "N:", len(alist)

    return alist

def find_smallest_index(any_list, len_list):
    """
        finds the smallest element in the list and returns its index
    """

    cost = 0

    smallest_i = float("inf")
    smallest_n = smallest_i

    for i in xrange(len_list):
        cost = cost + 1
        if any_list[i] < smallest_n:
            smallest_i = i
            smallest_n = any_list[i]

    # print "***find_smallest_index***:"
    # print "cost:", cost

    return smallest_i