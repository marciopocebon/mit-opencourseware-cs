import random

def insertion_sort_array_v1(unordered_list):
    """
        my implementation of an insertion sort algorithm using an array

        notes:
        - creates a new ordered list from the unordered list
        - does not swaps the elements in the un/ordered list
    """

    ordered_list = []
    ordered_list_len = 0

    while unordered_list != []:
        # gets the first element of the unordered_list
        top_item = unordered_list.pop(0)

        # L[n] > L[n+1]
        # inserts the item at the top of the list if it is the first to be inserted or is greater than the top one
        if ordered_list == [] or top_item > ordered_list[-1]:
            ordered_list.append(top_item)
            ordered_list_len = ordered_list_len + 1
        # otherwise, traverses the ordered list until it finds the correct slot
        else:
            i = ordered_list_len

            # until the whole ordered list is traversed
            while i > -1:
                # L[n-1] < L[n] < L[n+1]
                # inserts the item between L[n-1] and L[n+1]
                if top_item > ordered_list[i-1]:
                    ordered_list.insert(i, top_item)
                    ordered_list_len = ordered_list_len + 1
                    break;
                # L[n-1] == L[0]
                # inserts the item at the bottom of the list
                elif i-1 == 0:
                    ordered_list.insert(0, top_item)
                    ordered_list_len = ordered_list_len + 1
                    break;

                i = i - 1
        # debug
        # print ordered_list, unordered_list

    return ordered_list

def insertion_sort_array_v2(unordered_list):
    """
        implementation of an insertion sort algorithm using an array

        taken from: https://en.wikipedia.org/wiki/Insertion_sort
    """
    unordered_list_len = len(unordered_list)

    for i in xrange(1, unordered_list_len):
        j = i
        while j > 0 and unordered_list[j-1] > unordered_list[j]:
            # time cost
            # maybe, the swap can be done in a more efficiency way
            unordered_list[j], unordered_list[j-1] = unordered_list[j-1], unordered_list[j]
            j = j - 1

        # debug
        # print unordered_list
    return unordered_list

def insertion_sort_array_v3(unordered_list):
    """
        implementation of an insertion sort algorithm using an array

        taken from: https://en.wikipedia.org/wiki/Insertion_sort

        - moves A[i] position in one go
    """
    unordered_list_len = len(unordered_list)

    for i in xrange(1, unordered_list_len):
        x = unordered_list[i]
        j = i
        while j > 0 and unordered_list[j-1] > x:
            unordered_list[j] = unordered_list[j-1]
            j = j - 1

        unordered_list[j] = x

        # debug
        # print unordered_list

    return unordered_list