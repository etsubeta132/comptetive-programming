# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        for row in matrix:
            
            for num in row:
                heapq.heappush(heap, -num)
        
                if len(heap) > k:
                    heapq.heappop(heap)
            
        return -1 * (heap[0])
