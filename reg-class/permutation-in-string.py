class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l,r = 0,len(s1)-1
        sub_str = Counter(s2[l:r])
        target = Counter(s1)

    
        while r < len(s2):
            sub_str[s2[r]] = sub_str.get(s2[r],0)+1
            
            if sub_str == target:
                return True
            sub_str[s2[l]] = sub_str.get(s2[l],0)-1
            l+=1
            r+=1
        
        return False


        