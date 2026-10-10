class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        res = []
        comb = []

        # i is the location in digits
        def helper(i):
            if len(comb) == len(digits):
                res.append(comb.copy())
                return
            # for i in range(len(digits)):
            if i >= len(digits):
                return

            for j in range(len(keyboard[digits[i]])):
                comb.append(keyboard[digits[i]][j])
                helper(i + 1)
                comb.pop()
                helper(i + 1)

        helper(0)
        print(res)
        finalRes = ["".join(r) for r in res]
        return finalRes
