
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
        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        else:
            parent[rootx] = rooty
            rank[rooty] += 1

def union2(left, right):
    rk_rt = (left, 0)
    for i in range(left + 1, right + 1):
        if rank[i] > rk_rt[1]:
            rk_rt = (i, rank[i])
    
    for i in range(left + 1, right + 1):
        root = parent[i]
        parent[root] = rk_rt[0]
        if rk_rt[1] == rank[root]:
            rank[rk_rt[0]] += 1

n, q = list(map(int, input().split()))

parent = {i:i for i in range(1, n + 1)}
rank = {i:0 for i in range(1, n + 1)}

for i in range(q):
    type, x, y = list(map(int, input().split()))
    if type == 1:
        union(x, y)
    elif type == 2:
        union2(x, y)        
    else:
        print("YES" if find(x) == find(y) else "NO")