# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        heap = [-1* num for num in nums]
        heapify(heap)

        ans = 0
        for i in range(k):
            if nums:
                num = heapq.heappop(heap)
                ans += -1 * num
                heapq.heappush(heap, num - 1)
        
        return ans
        


        