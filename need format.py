def minimumTotal(triangle) -> int:
    height, width = len(triangle), len(triangle[-1])
    dp = [[0 for _ in range(width)] for _ in range(height-1)]
    dp.append(triangle[-1])

    for row in range(height-2, -1, -1):
        for col in range(width-(height-row)+1):
            dp[row][col] = min(dp[row+1][col],
                               dp[row+1][col+1])+triangle[row][col]

    return max(dp[0])


minimumTotal([[-1],
              [-2, -3]])