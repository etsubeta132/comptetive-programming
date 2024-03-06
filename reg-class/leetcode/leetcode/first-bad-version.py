# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 0,n
        mid = (left+right)//2

        while left <= right:
            if isBadVersion(mid):
                right = mid-1
                mid = (left+right)//2
            else:
                left = mid+1
                mid = (left+right)//2
        
        return left