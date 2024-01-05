class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0 , 0
        res = 0
        sett = set()
        while r < len(s):
            while s[r] in sett:
                l+=1
                sett = set(s[l:r])
            sett.add(s[r])
            res = max(res, r-l+1)
            r += 1
        return res



