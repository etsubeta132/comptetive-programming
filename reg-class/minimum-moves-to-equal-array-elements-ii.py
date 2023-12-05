class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        num_move_to = len(nums)//2
        for num in nums:
            moves=moves+abs(nums[num_move_to]-num)
        return  moves


        