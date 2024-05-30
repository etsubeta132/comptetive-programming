import sys, threading
from collections import defaultdict

def main():
    n, a, b, c = list(map(int, input().split()))
    memo = defaultdict(int)

    def dp(n):

        if  n == 0:
            return 0
        elif n < 0:
            return - float("inf")

        if n not in memo:
            memo[n] = max(dp(n - a), dp(n - b), dp(n - c)) + 1
        
        return memo[n]
    
    print(dp(n))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()