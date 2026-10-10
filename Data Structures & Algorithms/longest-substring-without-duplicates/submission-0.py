class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # At every point make sure to just keep moving forward if the current substring does not exist
        # Basically check the length of the substring in accordance to the right pointer
        # if the right pointer is matching the left pointer, we move the left pointer out of the way and add the right pointer
        # L, R = 0, 0
        # window = set()
        # while R < len(nums)

        # if len(s) == 1:
        #     return True
        # elif len(s) == 2:
        #     return 2 if s[0] != s[1] else 1
        if not s:
            return 0
        maxL = 1
        window = set()
        L,R = 0,0
        while L<=R and R < len(s):
            while L <= R and s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            maxL = max(maxL, R - L + 1)
            R += 1
        return maxL