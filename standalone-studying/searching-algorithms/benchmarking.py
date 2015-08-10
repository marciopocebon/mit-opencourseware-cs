import time

from binary_search import binary_search_v1, binary_search_tn, binary_search_v2
from linear_search import linear_search_v1, linear_search_v2, linear_search_v3
from exponential_search import exponential_search

num_trials = 10
input_size = 10**6
guess = input_size+2

def benckmark_search(array_list, x, method, num_runs):
    total = 0.0
    mean = 0.0
    worst_case = 0.0
    best_case = float("inf")

    for run in range(num_runs):
        start_time = time.time()

        method(array_list, x)

        time_taken = time.time() - start_time
        total += time_taken

        if time_taken < best_case:
            best_case = time_taken

        if time_taken > worst_case:
            worst_case = time_taken

    content = "%s \t | %.6f \t\t | %.6f \t\t | %.6f \t\t | %.6f \t\t | %s \n" % (method.__name__, total, total/num_runs, best_case, worst_case, len(array_list))
    f.write(content)

f = open('search-benchmarking.txt', 'w')
header = "method \t\t\t\t | total \t\t\t | mean \t\t\t | best_case \t\t | worst_case \t\t | input size \n"
f.write(header)

ordered_list = [x for x in xrange(input_size)]

# binary search
benckmark_search(ordered_list, guess, binary_search_tn, num_trials)
benckmark_search(ordered_list, guess, binary_search_v1, num_trials)
benckmark_search(ordered_list, guess, binary_search_v2, num_trials)

# exponential search
benckmark_search(ordered_list, guess, exponential_search, num_trials)

# linear search
benckmark_search(ordered_list, guess, linear_search_v1, num_trials)
benckmark_search(ordered_list, guess, linear_search_v2, num_trials)
benckmark_search(ordered_list, guess, linear_search_v3, num_trials)

f.close()