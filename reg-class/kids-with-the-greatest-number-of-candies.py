class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)
        greatest = []
        for i in candies:
            if i+extraCandies>=max_cand:
                greatest.append(True)
            else:
                greatest.append(False)
        return greatest


        