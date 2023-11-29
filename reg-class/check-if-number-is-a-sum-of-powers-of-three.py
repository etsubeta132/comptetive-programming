class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >=1:
            if n%3!=0 and n%3!=1:
                return False
            n= n//3
        return True




        