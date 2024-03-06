class Solution:
    def mySqrt(self, x: int) -> int:
        
        n = x
        while n*n > x:
            n//=2
        
        
        while (n+1)*(n+1) <= x:
            n+=1
        
        return n
        