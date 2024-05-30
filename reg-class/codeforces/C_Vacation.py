days = int(input())
happiness = []

for day in range(days):
    points = list(map(int, input().split()))
    happiness.append(points)


for i in range(days - 2, -1, -1):
    for j in range(3):
        res = 0
        for k in range(3):
            if k != j:
                res = max(res, happiness[i + 1][k])
        happiness[i][j] += res

print(max(happiness[0]))
            
