class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        cof = (num-3)%3
        if cof == 0:
            start = (num-3)/3
            return [start,start+1,start+2]
        else:
            return []