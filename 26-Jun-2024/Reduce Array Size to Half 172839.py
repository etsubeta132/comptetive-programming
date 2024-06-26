# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        heap = [-val for val in count.values()]
        heapq.heapify(heap)

        ln = 0
        size = 0

        while ln < len(arr)//2 and heap:
            freq = heapq.heappop(heap)
            ln += -1 * freq
            size += 1
        
        return size