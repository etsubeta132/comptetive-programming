class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        un = set(nums)
        curr = defaultdict(int)
        win = []
        l,r  = 0,len(nums)
        start = 0
        ctr = 0

        for j,val in enumerate(nums):  

            curr[val] += 1

            while len(curr) == len(un):
                ctr += r - j
                curr[nums[start]] -= 1
                if curr[nums[start]] == 0:
                    curr.pop(nums[start])
                start += 1
      
        return ctr