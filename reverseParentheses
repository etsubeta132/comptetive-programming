class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        while True:
            if "(" not in s:
                return s
            i,j=0,[]
            while i!=-1:
                if i==0:
                    j.append(0)
                i=s.find("(",i+1)
                if i!=-1:
                    j.append(i)
            x=s.find(")",j[-1])
            y=s[j[-1]+1:x][::-1]
            s=s.replace(s[j[-1]:x+1],y)
