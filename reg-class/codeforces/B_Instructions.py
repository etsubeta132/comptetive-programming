import sys, threading
from collections import defaultdict

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        memo = defaultdict(int)
        

        def dp(idx, res):

            if idx >= n:
                return res

            state = idx
            
            if state not in memo:
                foll = dp(nums[idx] + idx, res + nums[idx])
                pick = dp(nums[idx] + idx, nums[idx])
                notpick = dp(idx + 1, 0)
                
                
                memo[state] = max(foll, pick, notpick)
            
            return memo[state]
        
        ans = dp(0, 0)
        print(ans)




sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()