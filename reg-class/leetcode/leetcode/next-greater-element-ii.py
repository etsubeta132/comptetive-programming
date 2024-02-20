class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums+nums
        stack = []
        monoton = {}
        for idx,num in enumerate(nums2):
            while stack and num > stack[-1][0]:
                monoton[stack[-1]] = num
                stack.pop()
            stack.append((num,idx))
    
        res = []
        for i,num in enumerate(nums):
            res.append(monoton.get((num,i),-1))
        return res


                
