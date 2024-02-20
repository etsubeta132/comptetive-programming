class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0,len(s)-1
        def revStr(s,l,r):
            if l >= r:
                return s
            
            s[l],s[r] = s[r],s[l]
        
            l+=1
            r-=1
            return revStr(s,l,r)
        
        return revStr(s,l,r)
        
        