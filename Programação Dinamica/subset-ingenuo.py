from itertools import combinations
import time

def subset_sum_brute_force(nums, target):
    for r in range(len(nums) + 1):
        for subset in combinations(nums, r):
            if sum(subset) == target:
                return True, subset
    return False, []

def all_subset_sum_brute_force(nums, target):
    result = []
    for r in range(len(nums) + 1):
        for subset in combinations(nums, r):
            if sum(subset) == target:
                result.append(list(subset))
    return result

# start = time.time()
# print(subset_sum_brute_force(list(range(1, 25)), 200))

# end = time.time()
# print('{:.4f}'.format(end-start))

print(subset_sum_brute_force([2,3,7,8,10], 18))

print(all_subset_sum_brute_force([2,3,7,8,10], 18))

