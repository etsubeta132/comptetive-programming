class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        l,r = 0,len(piles)-1
        mx_piles = 0
        
        while l < r-1:
            
            mx_piles += piles[r-1]
            r-=2
            l+=1
        
        return mx_piles

        