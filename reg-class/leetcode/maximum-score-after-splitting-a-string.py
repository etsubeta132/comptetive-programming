class Solution:
    def maxScore(self, s: str) -> int:
        suffSum = [0]*len(s)
        prefSum = [0]*len(s)

        suffSum[-1] = int(s[-1])
        for i in range(len(s)-2,-1,-1):
            suffSum[i] = suffSum[i+1] + int(s[i])
        

        prefSum[0] = int(s[0])
        for i in range(1,len(s)):
            prefSum[i] = prefSum[i-1] + int(s[i])
        
        mxx = 0
        for i in range(len(s)-1):
            ones = suffSum[i+1]
            zeros = len(s[:i+1]) - prefSum[i]
            res = ones + zeros
            mxx = max(mxx,res)

        return mxx


            
        

        
