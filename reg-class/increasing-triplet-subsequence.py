class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return False

        else:
            mx = [n for n in nums]
        mn = [n for n in nums]
        
        for  i in range(len(nums)-2,0,-1):
            mx[i] = max(mx[i],mx[i+1])
        
        mx[0] = max(mx[0],mx[1])
        
        for j in range(1,len(nums)):
            mn[j] = min(mn[j],mn[j-1])
        
        
        for  i in range(len(nums)):
            if mn[i] < nums[i] < mx[i]:
                return True
        
        return False

        

        
