t = int(input())


for _ in range(t):
    strs = input()
    if len(strs) % 2 != 0:
        print("NO")
    else:
        n = len(strs)
        if strs[:n//2] != strs[n//2:]:
            print("NO")
        else:
            print("YES")
        