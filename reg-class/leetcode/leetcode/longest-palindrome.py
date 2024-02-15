class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        even = 0
        odd = 0
        odd2 = 0
        for key,val in counter.items():
            if val%2==0:
                even+=val
            else:
                odd += val-1
                odd2 = max(odd2,val)
        if odd2 != 0:
            odd = odd + 1
        return even + odd
        