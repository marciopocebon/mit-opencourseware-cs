def linear_search_v1(ordered_list, x):
    for y in ordered_list:
        if y == x:
            return True

    return False

def linear_search_v2(ordered_list, x):
    index = 0
    len_list = len(ordered_list)
    while index < len_list:
        if x == ordered_list[index]:
            return True

        index = index + 1

    return False

def linear_search_v3(ordered_list, x):
    index = 0
    len_list = len(ordered_list)

    for y in xrange(len_list):
        if x == ordered_list[index]:
            return True

    return False