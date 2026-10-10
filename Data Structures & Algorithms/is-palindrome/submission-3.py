class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                res += c
        if res == "":
            return True
        print(res)
        L, R = 0, len(res) - 1
        while L<R and res[L]==res[R]:
            print(res[L], res[R])
            L += 1
            R -= 1
        print(L, R, res[L], res[R])
        if L!=R and res[L]!=res[R]:
            return False
        else:
            return True