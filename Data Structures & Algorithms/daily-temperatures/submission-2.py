class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # [1, 4, 1, 2, 1, 0, 0]
        # Last el is always 0
        # 28
        # s = [28]

        # 40
        # prev = s = [28]
        # Keep making copies of the stack? mem issues
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
            # if found == True:
            #     res.append(days)
            # else:
            #     res.append(0)
            print("Temp: ", n, " Days: ", days)
            print("Stack: ", stack)
        return res[::-1]

