class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        print(dp)
        for i in range(len(nums) -1, -1, -1):
            print("Number in question: ", nums[i])
            for j in range(i):
                if nums[j] < nums[i] and dp[j] < dp[i] + 1:
                    dp[j] += 1
            print("After a run: ", dp)
        return max(dp)