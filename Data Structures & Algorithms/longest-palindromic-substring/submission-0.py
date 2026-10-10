class Solution:
    def longestPalindrome(self, s: str) -> str:
        # consider the cases for palindromes with 2 or 1 starting character
        if not s:
            return ""
        ans = ""
        def helper(L, R, s, ans):
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > len(ans):
                    ans = s[L : R+1]
                L -= 1
                R += 1
            return ans
        for i in range(0, len(s)):
            # Odd length traversal
            ans = helper(i, i, s, ans)
            
            # 2 member starting point
            ans = helper(i, i + 1, s, ans)

        return ans