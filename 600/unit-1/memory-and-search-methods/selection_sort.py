import sys

def selection_sort(L):
    """
        Sorts L in ascending order
        usage:
            L = [35, 4, 5, 29, 17, 58, 0]
            selection_sort(L)
                -> [0, 4, 5, 17, 29, 35, 58]
    """

    for i in range(len(L) - 1):
        min_index = i
        min_value = L[i]
        j = i + 1

        while j < len(L):
            if min_value > L[j]:
                min_value = L[j]
                min_index = j
            j += 1

        temp = L[i]
        L[i] = L[min_index]
        L[min_index] = temp
        print 'Partially sorted list = ', L

    return L

# elements = [35, 4, 5, 29, 17, 58, 0]
# print selection_sort(elements)