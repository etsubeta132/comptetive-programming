class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        checked = []
        to_check = [i for i in range(left,right+1)]
        for i in range(left,right+1):
            for rng in ranges:
                if rng[0] <=i<= rng[1]:
                    checked.append(i)
                    break
        return len(checked)==len(to_check)
        