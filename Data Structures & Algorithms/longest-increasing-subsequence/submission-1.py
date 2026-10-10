class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(0, i):
                if nums[j] < nums[i] and dp[j] < 1 + dp[i]:
                    dp[j] += 1
        return max(dp)