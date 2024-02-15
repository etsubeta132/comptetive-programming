class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l,r = 0,len(palindrome)-1
        if len(palindrome) <=1:
            return ""

        palindrome = [i for i in palindrome]
        while l<len(palindrome)-1:
            if palindrome[l] != "a" and l!=r:
                palindrome[l] = "a"
                return "".join(palindrome)
            l+=1
            r-=1
        if l == len(palindrome)-1 and palindrome[l] == "a":
            palindrome[l] = "b"
        
        return "".join(palindrome)
