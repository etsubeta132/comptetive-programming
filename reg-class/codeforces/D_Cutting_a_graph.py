
def find(x):
    while x != parent[x]:
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
    
n, m, k = list(map(int, input().split()))

parent = {i:i for i in range(1, n+1)}
rank = {i:0 for i in range(1, n+1)}

for i in range(m):
    x, y = list(map(int, input().split()))
    union(x, y)

for i in range(k):
    opp, x, y = list(input().split())
    x = int(x)
    y = int(y)
    if opp == "cut":
        rooty = find(y)
        rootx = find(x)
        if parent[y] == x:
            parent[y] = y
        
        elif parent[x] == y:
            parent[x] = x
        print(parent)
    else:
        print("YES" if find(x) == find(y) else "NO")
