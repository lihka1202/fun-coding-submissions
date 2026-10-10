class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromeRunner(start, end, ans):
            L,R = start, end
            while L>=0 and R < len(s) and s[L] == s[R]:
                ans += 1
                R += 1
                L -= 1
            return ans

        ans = 0
        for i in range(len(s)):
            ans = palindromeRunner(i, i, ans)
            ans = palindromeRunner(i, i+1, ans)
        return ans