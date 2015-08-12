from insertion_sort import

def shell_sort_v1(list):
    """
        my implementation of a shell sort with help from: https://www.cs.auckland.ac.nz/~jmor159/PLDS210/niemann/s_man.pdf
    """

    # TODO

def compute_h(N, h=1):
    """
        calculates the spacing h for an array of size N
    """

    if h <= N/9:
        return h

    return compute_h(N, (3*h) + 1)

list = []