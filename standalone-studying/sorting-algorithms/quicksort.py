import random

def quick_sort_v1(list):
    """
        my implementation of a quick sort algorithm with instructions from: http://web.mit.edu/1.124/LectureNotes/sorting.html
    """

    len_list = len(list)

    pivot = list[len_list/2]
    left = []
    right = []

    for x in list:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)

    print "pivot:", pivot
    print "left:", left
    print "right:", right

    # TODO