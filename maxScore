class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxPoint = 0
        for num in cardPoints[:k]:
            maxPoint += num
        currPoint = maxPoint
        for idx in range(k-1, -1, -1):
            currPoint += cardPoints[idx-k] - cardPoints[idx]
            maxPoint = max(maxPoint, currPoint)
        return maxPoint
