def maxSubarraySumCircular(A) -> int:
    cur_max = 0
    max_sum = A[0]
    cur_min = 0
    min_sum = A[0]

    for num in A:
        cur_max += num
        max_sum = max(max_sum, cur_max)
        if cur_max < 0:
            cur_max = 0

        cur_min += num
        min_sum = min(min_sum, cur_min)
        if cur_min > 0:
            cur_min = 0

    return max(max_sum, sum(A)-min_sum)


maxSubarraySumCircular([-2, -3, -1])