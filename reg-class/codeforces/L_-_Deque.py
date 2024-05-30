n = int(input())
values = list(map(int, input().split()))
maxMin = [[0]*(n + 1) for i in range(n + 1)]

for i in range(n):
    maxMin[i][i] = values[i]


for l in range(n - 1, -1, -1):
    for r in range(n):
        if l < r:
            left = values[l] - maxMin[l + 1][r]
            right = values[r] - maxMin[l][r - 1]
            maxMin[l][r] = max(left, right)


print(maxMin[0][n-1])

