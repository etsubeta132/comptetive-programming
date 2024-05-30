from collections import Counter
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    memo = {}
    counter = Counter(nums)

    def dp(num):

        if num < 0:
            return 0
        
        if num not in memo:
            memo[num] = max(dp(num - 1),  dp(num - 2) + num * counter[num]) 
        
        return memo[num]

    res = dp(max(nums))

    print(res)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()



    