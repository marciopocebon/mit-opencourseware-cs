import time
import random

from insertion_sort import insertion_sort_v1, insertion_sort_v2, insertion_sort_v3
from bubble_sort import bubble_sort_v1___, bubble_sort_v2___, bubble_sort_v3___
from selection_sort import selection_sort_v1, selection_sort_v2

num_trials = 1
input_size = 10**3
randomness = 10**10

def benckmark_search(array_list, method, num_runs):
    total = 0.0
    mean = 0.0
    worst_case = 0.0
    best_case = float("inf")
    array_list_len = len(array_list)

    for run in xrange(num_runs):
        cloned_list = array_list[:]

        start_time = time.time()
        method(cloned_list)
        time_taken = time.time() - start_time

        total += time_taken

        if time_taken < best_case:
            best_case = time_taken

        if time_taken > worst_case:
            worst_case = time_taken

    content = "%s \t | %.6f \t\t | %.6f \t\t | %.6f \t\t | %s \n" % (method.__name__, total, best_case, worst_case, array_list_len)
    f.write(content)

f = open('sort-benchmarking.txt', 'w')
header = "method \t\t\t\t | total \t\t\t | best_case \t\t | worst_case \t\t | input size \n"
f.write(header)

unordered_list = [random.randint(0, randomness) for x in xrange(input_size)]

# insertion sort
benckmark_search(unordered_list, insertion_sort_v1, num_trials)
benckmark_search(unordered_list, insertion_sort_v2, num_trials)
benckmark_search(unordered_list, insertion_sort_v3, num_trials)

# bubble sort
benckmark_search(unordered_list, bubble_sort_v1___, num_trials)
benckmark_search(unordered_list, bubble_sort_v2___, num_trials)
benckmark_search(unordered_list, bubble_sort_v3___, num_trials)

# selection sort
benckmark_search(unordered_list, selection_sort_v1, num_trials)
benckmark_search(unordered_list, selection_sort_v2, num_trials)

f.close()