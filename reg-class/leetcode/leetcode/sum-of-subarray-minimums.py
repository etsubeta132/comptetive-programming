class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        right = [0]*len(arr)
        left = [0]*len(arr)
        stack = []
        # number of elements btn the element and the smaller element to the right
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                right[idx] = i - idx
            stack.append(i)
        while stack:
            idx = stack.pop()
            right[idx] = len(arr)-idx
        
        # number of elements btn the element and the smaller element to the left
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                idx = stack.pop()
                left[idx] = idx - i
            stack.append(i)
        while stack:
            idx = stack.pop()
            left[idx] = idx - 0+1
        
        res = sum(left[i]*right[i]*arr[i] for i in range(len(arr)))
        mod = ((10**9)+7)               
        return res%mod