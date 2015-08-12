import sys

def bubble_sort_v1___(list):
    """
        my implementation of a bubble sort algorithm

        characteristics:
        - does not decreases the number of elements to be compared
    """

    cost = 0

    list_len = len(list)

    for turn in xrange(list_len):
        cost = cost + 1

        # swapping loop

        # time cost
        # once sorted, the last element does not need to be compared again in each iteration
        for n in xrange(list_len-1):
            cost = cost + 1
            # swap n by n+1
            if list[n] > list[n+1]:
                list[n+1], list[n] = list[n], list[n+1]

    print "***************"
    print sys._getframe().f_code.co_name
    print "N:", list_len
    print "running time:", cost
    print

    return list

def bubble_sort_v2___(list):
    """
        my implementation of a bubble sort algorithm

        improvements:
        - makes the 'swapping loop' smaller each turn
    """

    list_len = len(list)
    list_len_original = list_len

    cost = 0

    for turn in xrange(list_len):
        cost = cost + 1

        # swapping loop
        for n in xrange(list_len-1):
            cost = cost + 1
            # swap n by n+1
            if list[n] > list[n+1]:
                cost = cost + 1
                list[n+1], list[n] = list[n], list[n+1]

        # since we already sorted the last element, let's make the loop iteration smaller
        list_len = list_len - 1

    print "***************"
    print sys._getframe().f_code.co_name
    print "N:", list_len_original
    print "running time:", cost
    print

    return list

def bubble_sort_v3___(list):
    """
        an implementation of a bubble sort algorithm

        taken from: https://en.wikipedia.org/wiki/Bubble_sort
    """

    list_len = len(list)
    list_len_original = list_len

    cost = 0

    while list_len != 0:
        cost = cost + 1
        # swapping loop
        for n in xrange(1, list_len-1):
            cost = cost + 1
            # swap n by n+1
            if list[n-1] > list[n]:
                list[n-1], list[n] = list[n], list[n-1]
                list_len = n

        # since we already sorted the last element, let's make the loop iteration smaller
        list_len = list_len - 1

    print "***************"
    print sys._getframe().f_code.co_name
    print "N:", list_len_original
    print "running time:", cost
    print

    return list