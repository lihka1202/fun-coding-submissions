class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                res += c
        if res == "":
            return True
        return res == res[::-1]