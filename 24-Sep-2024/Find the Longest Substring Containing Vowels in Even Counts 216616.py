# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        dp = {0: -1}
        vowels ="aeiou"
        ans = parity = 0

        for idx, char in enumerate(s):
            if char in vowels:
                index = vowels.index(char)
                parity ^= 1 << index
            
            if parity in dp:
                ans = max(ans, idx - dp[parity])
            else:
                dp[parity] = idx

        return ans            