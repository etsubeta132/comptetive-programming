class Solution:
    def largestGoodInteger(self, num: str) -> str:
        un =["999","888","777","666","555","444","333","222","111","000"]
        for i in un:
            if i in num:
                return i
        return ""

        
            
