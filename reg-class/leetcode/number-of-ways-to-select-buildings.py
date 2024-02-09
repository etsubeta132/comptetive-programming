class Solution:
    def numberOfWays(self, s: str) -> int:
        before = [0]*len(s)
        after = [0]*len(s)

        ones = 0
        zeros = 0
        
        for i in range(len(s)):
            if s[i] == "1":
                before[i] += zeros
                ones+=1
            else:
                before[i] +=  ones
                zeros+=1
        

        ones = 0
        zeros = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                after[i] += zeros
                ones+=1
            else:
                after[i] +=  ones
                zeros+=1
        
        res = 0
        for i in range(len(s)):
            res += before[i]*after[i]
        
        return res

        