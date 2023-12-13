class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        str_dict = {}
        ctr = 0

        for char in s:
            if char not in str_dict:
                ctr+=1
                str_dict[char] =  1
      
        return ctr
        
