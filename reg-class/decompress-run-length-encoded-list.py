class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=0
        decomp = []
        while l<len(nums):
            decomp.extend([nums[l+1]]*nums[l])
            l+=2
        return decomp
            


        