class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_sq_digit(num):

            total = 0

            while num > 0:
                r = num % 10
                total += r**2
                num = num//10
            
            total+=num**2

            return total

        for i in range(100):
            n = sum_sq_digit(n)

            if n == 1:
                return True
        return False