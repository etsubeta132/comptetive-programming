class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = {}
        multi_nums = []
        for i in nums:
            if i in nums_count:
                nums_count[i]=nums_count[i]+1
            else:
                nums_count[i]=1
            if nums_count[i]>len(nums)/3 and i not in multi_nums:
                multi_nums.append(i)
        return multi_nums

        