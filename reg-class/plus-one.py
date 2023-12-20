class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ln = len(digits)-1
    
        while ln >= 0 and digits[ln] == 9:
            digits[ln] = 0
            ln-=1

        if ln == -1:
            digits.insert(0,1)
        else:
            digits[ln] += 1

        return digits