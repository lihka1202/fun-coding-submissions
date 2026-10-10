class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resSubsets = []
        subset = []
        def helper(i):
            # case where we exceed the values
            if i == len(nums):
                ## Need to ensure that this is the copy
                resSubsets.append(subset.copy())
            else:
                # Add to the path
                subset.append(nums[i])
                helper(i+1)

                ## Remove from the copy
                subset.pop()
                helper(i + 1)
        helper(0)
        return resSubsets
