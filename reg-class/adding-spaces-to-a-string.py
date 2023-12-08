class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ans = []
        left = 0

        for i in spaces:

            ans.append(s[left:i]+" ")
            left=i
        ans.append(s[i:])
        return "".join(ans)
