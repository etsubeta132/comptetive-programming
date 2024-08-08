# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count = [freq for freq in count.values()]
        count.sort(reverse = True)
        
        ln = l = 0
        while l < len(count) and ln < len(arr)// 2:
            ln += count[l]
            l += 1
        
        return l



        