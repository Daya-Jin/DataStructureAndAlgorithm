import sys

K = int(sys.stdin.readline().strip())
A, X, B, Y = map(int, sys.stdin.readline().split())
M = 1000000007


def func(K, A, X, B, Y):
    dp = [[0] * (K + 1) for _ in range(X + Y + 1)]
    w = [0] * (X + Y + 1)
    for i in range(1, X + 1):
        w[i] = A
    for i in range(X + 1, X + Y + 1):
        w[i] = B
    dp[0][0] = 1

    for i in range(1, X + Y + 1):
        for j in range(0, K + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i]:
                dp[i][j] += dp[i - 1][j - w[i]]
                dp[i][j] %= 1000000007

    return dp[-1][-1]


print(func(K, A, X, B, Y))
