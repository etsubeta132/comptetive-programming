class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}

        for i, num in enumerate(nums):
            compliment = target-num
            if compliment in result_dict:
                return [result_dict.get(compliment),i]
            
            result_dict[num] = i
        return None
        