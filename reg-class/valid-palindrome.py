class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(c for c in s if c.isalnum()).lower()
        x,y=0,len(s)-1
        while x<=y:
            if s[x]!=s[y]:
                return False
            else:
                x+=1
                y-=1
        return True
        