class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        mx = nums[0]
        prefSum  = nums[0]
        for idx in range(1,len(nums)):
            prefSum  += nums[idx]
            if nums[idx] > mx:
                avg = (prefSum//(idx+1)) if prefSum%(idx+1) == 0 else (prefSum//(idx+1))+1
                mx = max(mx,avg)

        return mx



