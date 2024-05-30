from collections import defaultdict
def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    rootx = find(x)
    rooty = find(y)

    if rootx != rooty:
        if rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
            mx = max(root[rootx][0], root[rooty][0], root[rooty][1])
            mn = min(root[rootx][1], root[rooty][1], root[rooty][0])
            sz = root[rootx][2] + root[rooty][2]
            root[rootx] = (mx, mn, sz)

        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
            mx = max(root[rootx][0], root[rooty][0], root[rootx][1])
            mn = min(root[rootx][1], root[rooty][1], root[rootx][0])
            sz = root[rootx][2] + root[rooty][2]
            root[rooty] = (mx, mn, sz)

        else:
            parent[rootx] = rooty
            mx = max(root[rootx][0], root[rooty][0], root[rootx][1])
            mn = min(root[rootx][1], root[rooty][1], root[rootx][0])
            sz = root[rootx][2] + root[rooty][2]
            root[rooty] = (mx, mn, sz)

n, m = list(map(int, input().split()))
parent  = {i:i for i in range(1, n+1)}
rank = {i:0 for i in range(1, n+1)}
root = defaultdict(tuple)


for i in range(1, n+1):
    root[i] = (i, i, 1)

for i in range(m):
    query = list(input().split())
    if query[0] ==  "union":
        union(int(query[1]), int(query[2]))
    else:
        rt = find(int(query[1]))
        print(root[rt][1], root[rt][0], root[rt][2])
        
