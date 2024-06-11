# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        count = Counter(arr1)
        result = []
        for num in arr2:
            if num in count:
                result += [num]*count[num]
                del count[num]
        
        rem = []
        for num in count.keys():
            rem += [num]*count[num]
            
        rem.sort()
        result += rem

        return result