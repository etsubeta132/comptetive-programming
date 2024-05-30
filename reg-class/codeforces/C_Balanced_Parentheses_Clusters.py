t = int(input())

def find(x):

    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(x, y):
    ry = find(y)
    rx = find(x)
    if rank[ry] > rank[rx]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1

for _ in range(t):
    n = int(input())
    inp = input()
    brackets = [i for i in inp]
    stack = []
    order = []
    l = 1
    for i in range(n*2):
        if brackets[i] == "(":
            stack.append((brackets[i], i))
        elif brackets[i] == ")":
            brack = stack.pop()
            order.append((brack[1],i+1))

    parent = {num[0]:num[0] for num in order}
    rank = {num[0]:0 for num in order}

    for i,j in order:
        if j < 2*n and brackets[j] == "(":
            union(i, j)

    result = set()
    for key, val in parent.items():
        val = find(val)
        result.add(val)

    print(len(result))