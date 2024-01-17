class NumArray:

    def __init__(self, nums: List[int]):
        self.nums  = nums
        self.total = [nums[0]]
        
        for i in range(1,len(nums)):
            res = self.nums[i] + self.total[i-1]
            self.total.append(res)

    def sumRange(self, left: int, right: int) -> int:
        
        return self.total[right] - self.total[left] + self.nums[left]





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)