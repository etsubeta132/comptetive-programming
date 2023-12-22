class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        



        if len(arr)<3:
            return False

        l = 0
        top = max(arr)
        idx = arr.index(top)
        if idx == len(arr) - 1 or idx == 0:
            return False

        while l < idx:
            if arr[l] >= arr[l+1]:
                return False
            l+=1
        

        while idx <= l <  len(arr)-1:
            if arr[l] <= arr[l+1]:
                return False
            l+=1
        
        return True