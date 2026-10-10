class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def palindromeGen(L, R, s, res):
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1
            return res
        for i in range(len(s)):
            res = palindromeGen(i,i,s,res)
            res = palindromeGen(i, i + 1, s, res)
        
        return res
            
        