class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)

        # Assume that for each case, we wish to store the
        # max approach in dp
        dp[-1] = nums[-1]
        dp[len(nums) - 2] = max(dp[-1], nums[len(nums) - 2])
        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(dp[i+2] + nums[i], dp[i+1])
        
        return max(dp[0], dp[1])