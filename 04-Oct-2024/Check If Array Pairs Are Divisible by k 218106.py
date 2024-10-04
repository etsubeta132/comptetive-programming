# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ctr = defaultdict(int)
        for num in arr:
            m =  num % k    
            r = (abs(k - m))%k
            if ctr[r] > 0:
                ctr[r]-= 1
            else:
                ctr[m]+=1
        
        for val in ctr.values():
            if val > 0:
                return False
        return True