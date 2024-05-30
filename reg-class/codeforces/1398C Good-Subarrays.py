from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input()))

    pref = 0
    freq = defaultdict(int)
    ctr = 0

    for i in range(n):
        cur = pref - i
        pref+=nums[i]

        isvalid = pref - i - 1
        freq[cur] +=1
        ctr += freq[isvalid]
    print(ctr)

