class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count_num =[0 for i in nums]
        for i in range(len(nums)):
            count = 0
            for j in nums:
                if j<nums[i]:
                    count+=1
            count_num[i] = count
        return count_num

            