class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        # The last one, for sure can pass it
        dp[-1] = True

        for i in range(len(nums) - 2, -1 , -1):
            if i + nums[i] > len(nums) - 1:
                dp[i] = True
            for j in range(1, nums[i] + 1):
                if (i + j) > (len(nums) - 1) or dp[i + j] == True:
                    dp[i] = True
                    break
            
        return dp[0]