class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        tot = sum(nums[0:k])
        avg = tot/k

        l,r = 0,k

        while r < len(nums):

            tot -= nums[l]
            tot += nums[r]

            avg = max(avg,tot/k)

            l+=1
            r+=1
        return avg