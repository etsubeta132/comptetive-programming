class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        target = Counter(p)
        window = Counter(s[:len(p)])

        ctr = []
        l,r = 0,len(p)
        if target == window:
            ctr.append(l)

        while r < len(s):
            
            
            first = s[l]
            end = s[r]

            window[first] -=1
            if window[first] == 0:
                del window[first]

            window[end]  = window.get(end,0) + 1
            l+=1
            r+=1
            if target == window:
                ctr.append(l)
        
        return ctr



