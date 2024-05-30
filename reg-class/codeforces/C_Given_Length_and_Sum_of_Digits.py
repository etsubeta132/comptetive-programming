
m, s = list(map(int, input().split()))

if int("9" *m) < s:
    print(-1, -1)
elif s == 0:
    if m == 1:
        print(0, 0)
    else:
        print(-1, -1) 
else:
    ans = ["0"]*m

    r = 0
    canFound = True

    while r < m and canFound:
        for j in range(9, -1, -1):
            if j <= s:
                if r == 0 and j == 0:
                    ans = ["-1"]
                    canFound = False
                    break
                else:
                    ans[r] = str(j)
                    s -= j
                    break
        r += 1

    small = ans[::-1] 
    large = ans

    if m > 0 and small[0] == "0":
        r = 0
        while r < m and small[r] == "0":
            r += 1
        
        if r < m:
            small[0], small[r] = small[r], small[0]
        else:
            small = ["-1"]
            large = ["-1"]

    print(int("".join(small)), int("".join(large)))      
        



