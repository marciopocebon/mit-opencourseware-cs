def linear_search_v1(ordered_list, x):
    for y in ordered_list:
        if y == x:
            return True

    return False

def linear_search_v2(ordered_list, x):
    index = 0
    while index <= len(ordered_list)-1:
        if x == ordered_list[index]:
            return True

        index = index + 1

    return False