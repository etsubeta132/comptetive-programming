class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        res = set()
        l,r = 0,0

        while r < len(nums2) and l<len(nums1):
            if nums1[l]==nums2[r]:
                res.add(nums1[l])
                l+=1
                r+=1
            
            elif nums1[l]>nums2[r]:
                r+=1
            else:
                l+=1
        
        return res


