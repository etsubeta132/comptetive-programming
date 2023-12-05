class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        suffled_str = [""]*len(s)
        
        for idx,val in enumerate(s):
            suffled_str[indices[idx]]=val

        suffled_str = "".join(suffled_str)
        return suffled_str

