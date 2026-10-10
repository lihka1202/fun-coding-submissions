class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Init larger to hold the final state
        dp = [False] * (len(s) + 1)
        
        # Set the final case to be true, since if you reach here you can certainly form this string
        dp[len(s)] = True

        for i in range(len(s) -1, -1 ,-1):
            for word in wordDict:
                ## Checks if the word is outside the range of s, and ensure that its the word we're looking for
                if (i + len(word)) <= len(s) and s[i : i+len(word)] == word:
                    # need to ensure that this chain is connected 
                    dp[i] = dp[i + len(word)]
                
                ## Check if we found some word
                if dp[i]:
                    break
        print(dp)
        return dp[0]