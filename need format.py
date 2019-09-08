def numPermsDISequence(S: str) -> int:
    n = len(S) + 1
    mod = 1e9 + 7
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][0] = 1
    for i in range(2, n + 1):
        for j in range(i):
            if S[i - 2] == 'I':
                dp[i][j] = int(sum(dp[i - 1][:j]) % mod)
            else:
                dp[i][j] = int(sum(dp[i - 1][j:]) % mod)

    return int(sum(dp[-1]) % mod)
