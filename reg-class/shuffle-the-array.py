class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_axis = nums[:n]
        y_axis = nums[n:]
        shuffled = []
        for i in range(len(x_axis)):
            shuffled.append(x_axis[i])
            shuffled.append(y_axis[i])
        return shuffled
        