def wordBreak(s: str, wordDict) -> bool:
    if not s:
        return True

    wordDict = set(wordDict)

    n = len(s)
    dp = [False for _ in range(n + 1)]  # dp[0]对应空字串
    dp[0] = True
    for tail in range(1, n + 1):
        for cut in range(0, tail + 1):
            right_s = s[cut:tail]
            if dp[cut] == True and s[cut:tail] in wordDict:
                dp[cut] = True
                break
    return dp[-1]


wordBreak("leetcode", ["leet", "code"])