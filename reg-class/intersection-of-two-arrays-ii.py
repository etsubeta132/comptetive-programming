class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        nums = []

        for num in nums1.keys():
            if num in nums2:
                mn = min(nums2[num],nums1[num])
                nums.extend([num]*mn)
        
        return nums
