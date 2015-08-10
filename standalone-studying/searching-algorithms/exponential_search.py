from binary_search import binary_search_tn

def exponential_search(ordered_list, x):
    """
        implementation of an exponential search algorithm
        taken from: https://en.wikipedia.org/wiki/Exponential_search
    """

    list_size = len(ordered_list)

    bound = 1

    while bound*2 < list_size and ordered_list[2*bound-1] < x:
        bound = bound * 2

    return binary_search_tn(ordered_list, x, bound)