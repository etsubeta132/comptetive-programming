class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)

        mn = 0
        l,r = 3,0
        while r < len(processorTime):
            res = tasks[l] + processorTime[r]
            mn = max(mn,res)
            l+=4
            r+=1
        
        return mn


