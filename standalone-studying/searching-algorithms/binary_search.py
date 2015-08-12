def binary_search_tn(ordered_list, x, Ub=0):
    """
        iterative implementation of a binary search algorithm

        'tn' stands for thomas niemann, the author

        taken from: https://www.cs.auckland.ac.nz/~jmor159/PLDS210/niemann/s_man.pdf
    """

    Lb = 0


    if Ub == 0:
        Ub = len(ordered_list)-1

    while True:
        M = (Lb+Ub)/2

        if x < ordered_list[M]:
            Ub = M - 1
        elif x > ordered_list[M]:
            Lb = M + 1
        else:
            return True

        if Lb > Ub:
            return False

def binary_search_v1(ordered_list, x):
    """
        recursive implementation of a binary search algorithm
        - computes the size of the list in every [recursive] call
        - rebuilds the list in every [recursive] call
    """
    # my first implementation

    # time impact
    # every time the function is called, it computes the size of the array
    size = len(ordered_list)

    m = size/2

    if size > 1:
        if x < ordered_list[m]:
            # time impact
            # resizing the array
            return binary_search_v1(ordered_list[:m], x)
        elif x > ordered_list[m]:
            # time impact
            # resizing the array
            return binary_search_v1(ordered_list[m:], x)
        else:
            return True
    else:
        if x == ordered_list[m]:
            return True
        else:
            return False

def binary_search_v2(ordered_list, x):
    """
        recursive implementation of a binary search algorithm
        - computes the size of the array, only once
        - do not rebuilds the array
    """

    # my implementation without array resizing + learnings from binary_search_tn
    # initializes the indexes
    start_index = 0
    end_index = len(ordered_list)-1

    # time impact
    # maybe the recursion is delaying the processing, see benchmark result for details
    # inner function to be run recursively
    def inner_runner(start_index, end_index):
        if start_index > end_index:
            return False

        middle_index = (start_index+end_index) / 2

        if x < ordered_list[middle_index]:
            return inner_runner(start_index, middle_index-1)
        elif x > ordered_list[middle_index]:
            return inner_runner(middle_index+1, end_index)
        else:
            return True

    return inner_runner(start_index, end_index)