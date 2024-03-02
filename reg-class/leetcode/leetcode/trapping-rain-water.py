class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        area = 0
        l,r = 0,len(height)-1
        lmx,rmx = height[l],height[r]
        while l < r :
            if lmx< rmx:
                l+=1
                lmx = max(lmx,height[l])
                area+= lmx - height[l]
            else:
                r-=1
                rmx = max(rmx,height[r])
                area += rmx - height[r]
        return area
