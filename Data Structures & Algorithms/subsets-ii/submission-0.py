class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []
        nums.sort()
        def helper(i):
            # if i is the same as the length of nums
            if i == len(nums):
                res.append(s.copy())
            else:
                ## Consider the current number in the path
                s.append(nums[i])
                helper(i + 1)

                # Don't consider this in the path at all
                # Since its duplicate, need to ensure that you skip all the duplicates
                while i + 1< len(nums) and nums[i] == nums[i+1]:
                    i += 1
                s.pop()
                helper(i+1)
        helper(0)
        return res