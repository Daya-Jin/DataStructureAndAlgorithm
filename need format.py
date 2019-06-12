def numSquares(n: int) -> int:
    dp = [4]*(n+1)
    dp[0] = 0

    for i in range(n+1):
        for base in range(1, int(n**0.5)+1):    # 完全平方数的基数
            new_num = i+base**2
            if new_num <= n:
                # 从dp[i]到dp[i+base**2]只加了一个完全平方数
                dp[new_num] = min(dp[new_num], dp[i]+1)

    return dp[-1]


numSquares(12)
