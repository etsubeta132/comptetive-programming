# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        ctr = 0
        num = target
        while num > startValue:
            if num % 2 == 0:
                ctr +=1
                num = num //2
            else:
                ctr += 2
                num = (num //2 ) + 1
            
        if num == startValue:
            return ctr
        else:
            return ctr + (startValue - num)