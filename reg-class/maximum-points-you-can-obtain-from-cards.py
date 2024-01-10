class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        l,r= 0,k-1
        total = 0
        for i in range(k):
            total+=cardPoints[i]
        
        res = total
        r = k-1
        while r >= 0:
            res += cardPoints[r-k] - cardPoints[r]
            total = max(total,res)
            r-=1

        return total
            