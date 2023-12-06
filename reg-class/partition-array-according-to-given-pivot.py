class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater_pivot = []
        equal_pivot = []
        less_pivot = []
        for num in nums:
            if num > pivot:
                greater_pivot.append(num)
            elif num< pivot:
                less_pivot.append(num)
            else:
                equal_pivot.append(num)
        paritioned_arr =  less_pivot + equal_pivot + greater_pivot
        return paritioned_arr
