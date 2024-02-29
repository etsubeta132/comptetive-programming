class Solution:
    def longestNiceSubstring(self, s: str) -> str:
    
        def divide(start,end):
            if end - start + 1 < 2:
                return (0,-1)

            part = set(s[start:end+1])

            for i in range(start,end+1):
                if s[i].upper() in part and  s[i].lower() in part:
                    continue

                s_left =  divide(start,i-1)
                s_right  = divide(i+1,end)

                return s_left if (s_left[1] - s_left[0] + 1) >= ( s_right[1] -  s_right[0] + 1) else  s_right

            return (start,end)
        start,end  = divide(0,len(s)-1)
        return s[start:end+1]


            

