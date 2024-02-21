class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        else:
            return pow(x,n-1)*x

