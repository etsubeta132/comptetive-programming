class Solution:
    def minimumSteps(self, s: str) -> int:
        ctr = 0
        zeros= 0
        for i in range(len(s)-1,-1,-1):
            ball = s[i]
            if ball == "0":
                zeros+=1
            else:
                ctr+=zeros   
                     
        return ctr
