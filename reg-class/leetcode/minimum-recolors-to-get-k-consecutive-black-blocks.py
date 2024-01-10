class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l,r = 0,k-1
        opps = float ('inf')
        res = 0
        for i in range(k-1):
            if blocks[i] == "W":
                res+=1
        
        while r < len(blocks):
            if blocks[r] == "W":
                res+=1
            opps = min(res,opps)

            if blocks[l] == "W":
                res-=1
            
            l+=1
            r+=1
        return opps
            