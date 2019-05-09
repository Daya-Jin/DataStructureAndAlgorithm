def rob(nums) -> int:
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)

    def rob_max(nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = 0
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    nums_1 = nums[1:]
    nums_2 = nums[:-1]
    return max(rob_max(nums_1), rob_max(nums_2))


rob([1, 2, 3, 1])