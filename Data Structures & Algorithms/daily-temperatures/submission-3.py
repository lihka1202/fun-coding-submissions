class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]
        stack = [temperatures[-1]]
        for n in temperatures[::-1][1:]:
            cp = stack.copy()
            days = 1
            found = False
            while(len(cp) > 0 and n >= cp[-1]):
                days += 1
                cp.pop()
            if len(cp) == 0:
                days = 0
            stack.append(n)
            res.append(days)
        return res[::-1]

