# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        i, j, res = 0, 1, 1
        while j < len(prices):
            if prices[j] == prices[j - 1] - 1:
                res += (j - i + 1)
            else:
                i = j
                res += 1
            j += 1

        return res