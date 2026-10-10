class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        dct = {}
        maxi = 1
        for n in nums:
            dct[n] = False
        for key in dct.keys():
            if dct[key] == True:
                # Already part of some sequence
                continue
            dct[key] = True
            count = 1
            move = key + 1
            while move in dct:
                # print(key + 1)
                dct[move] = True
                count += 1
                maxi = max(count, maxi)
                move += 1
        
        print(dct)
        print(maxi)
        return maxi
        