# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution(object):
    def kthLargestNumber(self, nums, k):
        
        list.sort( nums,reverse=True, key=int)
        return nums[k-1]