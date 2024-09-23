# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = defaultdict(int)
       
        def dp(idx, isbuyed):

            if idx >= len(prices):
                return 0
            
            state = (idx, isbuyed)

            if state not in memo:
                notpick = dp(idx + 1, isbuyed)
                if isbuyed:
                    pick = prices[idx] + dp(idx + 2, False)
                else:
                    pick = (-1 * prices[idx]) + dp(idx + 1, True)
                
                memo[state] = max(pick, notpick)
            
            
            return memo[state]
        
        return dp(0, False)