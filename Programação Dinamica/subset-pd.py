import time
def subset_sum_dp_solution(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]

    if not dp[n][target]:
        return False, []

    # Recuperar subconjunto
    subset = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i-1][j]:
            subset.append(nums[i-1])
            j -= nums[i-1]
        i -= 1
    return True, subset[::-1]

def all_subset_sum_dp_solution(nums, target):
    n = len(nums)
    dp = [[[] for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0] = [[]]  # Só há um subconjunto (o vazio) que soma a 0

    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = list(dp[i-1][j])  # Não inclui nums[i-1]
            if j >= nums[i-1]:
                for subset in dp[i-1][j - nums[i-1]]:
                    dp[i][j].append(subset + [nums[i-1]])

    return dp[n][target]


# start=time.time()
# print(subset_sum_dp_solution(list(range(1, 25)), 200))
# end = time.time()
# print('{:.4f}'.format(end-start))

print(all_subset_sum_dp_solution([2,3,7,8,10],11))