class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        ctr = 0
        max_n = 0
        for idx in range(len(flips)):
            max_n = max(max_n,flips[idx])
            if max_n == idx+1:
                ctr+=1
        
        return ctr
               
