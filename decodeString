class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur = ""
        k = 0
        for c in s:
            if c == "[":
                stack.append((cur, k))
                cur, k = "", 0
            elif c == "]":
                enc, n = stack.pop()
                cur = enc + n * cur 
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                cur += c
            print(k)
        return cur
