# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            num = str(nums[i])
            new_num = []
            for i in range(len(num)):
                idx = int(num[i])
                new_num.append(str(mapping[idx]))
            res.append(int("".join(new_num)))
        
        zipped_pairs = zip(res, nums)
        new_nums = sorted(zipped_pairs, key = lambda num : num[0])

        return [x for _,x in new_nums]


