# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        if n == 1:
            return True
    
        return n%2==0 and self.isPowerOfTwo(n/2)
        

