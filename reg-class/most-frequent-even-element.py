class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums_count = {}
        multi_nums = []
        max_count = 0
        for num in nums:
            if num%2==0:
                if num in nums_count:
                    nums_count[num]+=1
                else:
                    nums_count[num]=1
                new_num = int(nums_count[num])
                max_count = max(new_num,max_count)
        if nums_count=={}:
            return -1
        else:
            min_num = float('inf')
            for num in nums_count:
                if nums_count[num]==max_count:
                    min_num = min(min_num,num)
            return min_num       

        