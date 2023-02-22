class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        status = []
        
        for i in range(len(l)):
            isArthematic = True
            subList = nums[l[i]:r[i]+1]
            subList.sort()
            for j in range(len(subList)-1):
                if subList[1]-subList[0] != subList[j+1]-subList[j]:
                    isArthematic = False
            status.append(isArthematic)
        return status
