from insertion_sort import

def shell_sort_v1(unodered_list):
    """
        my implementation of a shell sort with help from: https://www.cs.auckland.ac.nz/~jmor159/PLDS210/niemann/s_man.pdf
    """

    list_len = len(unodered_list)
    h = compute_h(list_len)

    # TODO - continue implementation

def compute_h(N, h=1):
    """
        calculates the spacing h for an array of size N
    """

    if h >= N:
        return h

    return compute_h(N, (3*h) + 1)

print compute_h(100)