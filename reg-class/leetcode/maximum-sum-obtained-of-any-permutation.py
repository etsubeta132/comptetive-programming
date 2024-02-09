class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0]*(len(nums)+1)

        for start,end in requests:
            pref[start] +=1
            pref[end+1] -=1

        for i in range(1,len(nums)+1):
            pref[i]+=pref[i-1]
        
        pref.pop()
        pref.sort()
        nums.sort()
        
        res = [a*b for a,b in zip(pref,nums)]
        result = sum(res)

        return result %((10**9) + 7)
            
            
