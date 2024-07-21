# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:

        @cache 
        def dp(idx):

            if idx == len(s):
                return 1
            
            take1 = take2 = 0
            if int(s[idx]) != 0:
                take1 = dp(idx + 1)
            
                if idx + 1 < len(s) and int(s[idx : idx + 2]) <= 26:
                    take2 = dp(idx + 2)
            
            
            return take1 + take2
        
        return dp(0)

        