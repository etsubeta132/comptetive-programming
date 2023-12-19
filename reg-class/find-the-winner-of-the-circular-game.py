class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        

        n_list  = [i for i in range(1,n+1)]
        ctr = 0
        while len(n_list) > 1:
            ctr+=k-1

            if ctr >= len(n_list):

                ctr = ctr % len(n_list)

            n_list.pop(ctr)

        return n_list[-1]
            
