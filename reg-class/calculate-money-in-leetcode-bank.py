class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        total_money=0
        num_weeks = n//7
        left_days = n%7

        for i in range(num_weeks):
            total_money += (( 7*( 2*monday+6 ) )/2)
            monday+=1

        total_money += (( left_days*( 2*monday+left_days-1 )) /2)
        return int(total_money)


        