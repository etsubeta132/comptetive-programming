class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels =set()
        v = ["a","e","i","o","u"]
        for i in v:
            vowels.add(i)
        mxV = 0
        ctr = 0
        l,r = 0,0
        while r < k-1:
            if s[r] in vowels:
                ctr+=1
            r+=1
        
        while r < len(s):
            if s[r] in vowels:
                ctr+=1
            
            mxV = max(ctr,mxV)

            if s[l] in vowels:
                ctr-=1

            l+=1
            r+=1
        
        return mxV





        
