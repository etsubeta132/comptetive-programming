class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        """
        """
        ctr = 0
        while target > 1:
            if target%2 != 0:
                target-=1
            else:
                if maxDoubles:
                    target  = target//2
                    maxDoubles-=1
                else:
                    ctr += target-1
                    return ctr
            ctr+=1

        return ctr