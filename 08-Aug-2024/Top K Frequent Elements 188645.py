# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-freq, elem) for elem, freq in count.items()]
        heapq.heapify(heap)

        ans = []
        while k > 0 and heap:
            freq, elem = heapq.heappop(heap)
            ans.append(elem)
            k -= 1
        
        return ans


        