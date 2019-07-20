def ranking(n: int) -> int:
    if n < 0:
        return -1

    dp = [[0] * n for _ in range(n)]
    for row in range(n):
        dp[row][0] = 1
    for col in range(n):
        dp[0][col] = 1
    for idx in range(1, n):
        dp[idx][idx] = dp[idx-1][idx-1]*(idx + 1)

    for row in range(1, n):
        for col in range(1, n):
            if row==col:
                dp[row][col]=dp[row-1][col-1]*(row+1)
            else:
                dp[row][col] = (col + 1) * dp[row - 1][col] + (col + 1) * dp[row - 1][col - 1]

    res = 0
    for col in range(n):
        res += dp[-1][col]

    return res


print(ranking(2))
