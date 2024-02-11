class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        r = 0
        num = 0
        isDivisible = []
        for i in range(len(word)):

            num = (r*10+int(word[i]))%m
            r = num%m
            if r == 0:
                isDivisible.append(1)
            else:
                isDivisible.append(0)
        
        return isDivisible

