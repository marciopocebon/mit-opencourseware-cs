def single_merge_wrapper(index, L, merged_list):
    while index < len(L):
        value = L[index]
        merged_list.append(value)
        index += 1

    return index, merged_list

def double_merge_wrapper(l1_index, L1, l2_index, L2, merged_list, cb):
    while l1_index < len(L1) and l2_index < len(L2):
        value_l1 = L1[l1_index]
        value_l2 = L2[l2_index]

        if cb(value_l1, value_l2):
            merged_list.append(value_l1)
            l1_index += 1
        else:
            merged_list.append(value_l2)
            l2_index += 1

    return l1_index, l2_index, merged_list

def merge_sort(L1, L2, cb):
    """
        Given two sorted lists, merges them quickly
        usage:
            list_1 = [1, 5, 12, 18, 19, 20]
            list_2 = [2, 3, 4, 17]
            merge_sort(list_1, list_2, cb)
            -> [1, 2, 3, 5, 4, 12, 17, 18, 19, 20]
    """
    l1_index, l2_index, merged_list = 0, 0, []

    # merges both lists
    l1_index, l2_index, merged_list = double_merge_wrapper(l1_index, L1, l2_index, L2, merged_list, cb)

    # merges remaining elements from lists
    l1_index, merged_list = single_merge_wrapper(l1_index, L1, merged_list)
    l2_index, merged_list = single_merge_wrapper(l2_index, L2, merged_list)

    return merged_list

def sort(L, cb = lambda x, y: x < y):
    """
        Sorts the list L using the merge sort algorithm
    """

    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = sort(L[:middle], cb)
        right = sort(L[middle:], cb)
        print 'About to merge', left, 'and', right

        return merge_sort(left, right, cb)

# L = [35, 4, 5, 29, 17, 58, 0]
# L = [1.0, 2.25, 24.5, 12.0, 2.0, 23.0, 19.125, 1.0]
# print sort(L, float.__gt__)
# print sort(L, float.__lt__)
# print sort(L, lambda x,y: x > y)