class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        m = len(operations)
        n = len(nums)

        num_idx = {num:i for i,num in enumerate(nums)}
        idx_num = {i:num for i,num in enumerate(nums)}

        for operation in operations:
            num = operation[0]
            rpls = operation[1]

            idx = num_idx[num]

            idx_num[idx] = rpls

            num_idx[rpls] = idx
        
            del num
            
        new_num = idx_num.values()

        return new_num
