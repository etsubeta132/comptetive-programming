class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l,r = 0,0
        med  = len(nums1)+len(nums2)
        merged = []

        while l<len(nums1) and r<len(nums2):
            if nums1[l] <= nums2[r]:
                merged.append(nums1[l])
                l+=1
            else:
                merged.append(nums2[r])
                r+=1
        
        while l<len(nums1):
            merged.append(nums1[l])
            l+=1
        
        while r<len(nums2):
            merged.append(nums2[r])
            r+=1
        
        if med%2==0:
            med = [med//2-1,med//2]
            median = (merged[med[0]]+merged[med[1]])/2
        else:
            med = med//2
            median = merged[med]
            
        return median



            


            

                


            


