
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

n = int(input())
nums = list(map(int, input().split()))
parent = {i+1:i+1 for i in range(n)}
rank = {i+1:0 for i in range(n)}

for i in range(n):
    num = nums[i]
    union(i+1, num)

result = set()
for key, val in parent.items():
    val = find(val)
    result.add(val)

print(len(result))


vowels = {"a","e", "i","o",u}


stack = []

for c in word:
    if stack and stack[-1] in vowels and c in vowels:
            continue
    else:
        stack.append(c)
        






    

    