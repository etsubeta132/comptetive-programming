# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        heapq.heapify(heap)

        tot = 0
        l = 1
        while l < len(heights): 
            if heights[l] > heights[l - 1]:
                rg = heights[l] - heights[l - 1]
                if len(heap) < ladders:
                    heapq.heappush(heap, rg)
                else:
                    if heap:
                        sm = heapq.heappop(heap)
                        heapq.heappush(heap, max(rg, sm))
                        tot += min(rg, sm)  
                    else:
                        tot += rg
            
                if tot > bricks:
                    return l - 1
            
            l += 1 
 
        return len(heights) - 1
        
                
        