from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        stack  = []
        l,r = 0,0
        ans = 0
        while r < len(nums):
            sl.add(nums[r])
            stack.append(nums[r])
            while abs(sl[-1] - sl[0]) > limit:
                num = stack.pop(0)
                sl.remove(num)
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
            
                    
            

                    
                    

