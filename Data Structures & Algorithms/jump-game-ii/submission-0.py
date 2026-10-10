class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [10001] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i], -1 , -1):
                if i + j >= len(nums) - 1:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], 1 + dp[i + j])
        print(dp)
        return dp[0]