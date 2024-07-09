# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
array = [0] + list(map(int, input().split()))

position = 1

while position <= n:
    if position == t:
        print("YES")
        break
    position += array[position] if position < n else 1
else:
    print("NO")
