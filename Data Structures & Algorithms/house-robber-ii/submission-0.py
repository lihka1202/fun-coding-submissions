class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        robone = nums[1:]
        robtwo = nums[0: len(nums) - 1]
        dpone = [0] * len(robone)
        dptwo = [0] * len(robtwo)
        if not robone:
            return 0
        if len(robone) <= 2:
            return max(max(robone), max(robtwo))
        def calculatedp(dp, nums):
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            # print(dp)
            return dp[-1]          
          
        return max(calculatedp(dpone, robone), calculatedp(dptwo, robtwo))