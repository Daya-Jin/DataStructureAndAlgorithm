# 思路：动态规划的典型例子
# 设硬币可能的面额为denomination，状态转移方程为dp[i]=min(dp[i],dp[i-denomination]+1)
# 关键在于动态数组的初始化，将所有位置初始化为一个大值


def coinChange(coins, amount: int) -> int:
    if not coins:
        return -1
    if amount == 0:
        return 0

    max_val = 1e8
    dp = [max_val for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for denomination in coins:
            if denomination <= i:
                dp[i] = min(dp[i], dp[i - denomination] + 1)

    return dp[-1] if dp[-1] != max_val else -1


coinChange([1, 2, 5], 11)