class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        colors = {}
        res = 0
        for r in answers:
            if r in  colors:
                if colors[r] == r+1:
                    res+=colors[r]
                    del colors[r]
                    colors[r] = 1
                else:
                    colors[r]+=1
            else:
                colors[r] = 1
        
        for i in colors.keys():
            res+=i+1
        return res            

