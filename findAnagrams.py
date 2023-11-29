class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        pCounter,sCounter={},{}
        for i in range(len(p)):
            pCounter[p[i]]=1+pCounter.get(p[i],0)
            sCounter[s[i]]=1+sCounter.get(s[i],0)
        result=[0] if pCounter==sCounter else []
        left=0
        for right in range(len(p),len(s)):
            sCounter[s[right]]=1+sCounter.get(s[right],0)
            sCounter[s[left]]-=1
            
            
            if sCounter[s[left]]==0:
                sCounter.pop(s[left])
            left=left+1
            
            
            if sCounter==pCounter:
                result.append(left)
            
            

            
        return result
