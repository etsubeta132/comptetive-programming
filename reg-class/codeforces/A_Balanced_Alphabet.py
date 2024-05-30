t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = ''
    for i in range(n):
        s += chr(ord('a') + (i % k))
        
    print(s)
