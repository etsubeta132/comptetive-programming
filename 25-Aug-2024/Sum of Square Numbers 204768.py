# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        r  = int(c**(1/2)) + 1
        l = 0
         
        while l <= r:
            ans = l **2 + r ** 2
            if ans == c:
                return True
            elif ans < c:
                l += 1
            else:
                r -= 1
        return False      
        