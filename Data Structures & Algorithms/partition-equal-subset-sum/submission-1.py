class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Main idea, need to check if its even possible to reach half the sum first
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        # not possible to split if the sum is not even
        for n in nums:
            dp_copy = set()
            for num in dp:
                dp_copy.add(num)
                dp_copy.add(num + n)
            dp = dp_copy
        return True if (sum(nums)/2) in dp else False

