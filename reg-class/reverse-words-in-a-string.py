class Solution:
    def reverseWords(self, s: str) -> str:
        # s.strip()
        str_list = s.split()
        new_str = str_list[::-1]

        new_s = " ".join(new_str)
        
        return new_s
