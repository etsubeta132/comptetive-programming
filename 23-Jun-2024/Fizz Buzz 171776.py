# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype = []
        for i in range(n):
            j=i+1
            if j%3==0 and j%5==0:
                rtype.append("FizzBuzz")
            elif j%3==0:
                 rtype.append("Fizz")
            elif j%5==0:
                 rtype.append("Buzz")
            else:
               
                rtype.append(str(j))
        return  rtype
sol =  Solution()
sol.fizzBuzz(5)
