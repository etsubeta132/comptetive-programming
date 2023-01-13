class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
                return False
        if n==1:
            return True
        return n%3==0 and self.isPowerOfThree(n/3)
