class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplet = set()
        n= len(nums)
        

        for m in range(n-2):
            l = m+1
            r = n-1
            while l<r:
                res = nums[l]+nums[m]+nums[r]
                if res == 0:
                    triplet.add((nums[l],nums[m],nums[r]))
                    l+=1
                elif res>0:
                    r-=1
                else:
                    l+=1
            
        return triplet
            
