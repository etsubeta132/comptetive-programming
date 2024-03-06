class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left,right = 0,len(nums)-1
        idx = (left+right)//2
        while 0<= left <= right < len(nums):
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                right = idx - 1
            else:
                left = idx + 1
            idx = (left+right)//2

        return left
            



        