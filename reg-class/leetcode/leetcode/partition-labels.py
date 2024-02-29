class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition = {}
        for i in range(len(s)):
            partition[s[i]] = i
        
        mx = 0
        j = 0
        ans = []

        for i in range(len(s)):
            mx = max(mx,partition[s[i]])
            if mx == i:
                ans.append(i-j+1)
                j = i+1 
        
        return ans