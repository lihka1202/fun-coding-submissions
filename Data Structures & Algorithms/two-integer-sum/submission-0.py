class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {num : [idx]}
        dct = {}
        for idx,num in enumerate(nums):
            if num not in dct:
                dct[num] = []
            dct[num].append(idx)

        res = set()
            
        for idx,num in enumerate(nums):
            if target-num in dct:
                for index in dct[target-num]:
                    if index != idx:
                        res.add(index)
                        res.add(idx)
                        break
        res = list(res)
        res.sort
        print(res)
        return res
        # res = list(res)
        # res = res.sort()
        # return res