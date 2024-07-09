# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict, deque

def mi():
    return list(map(int, input().split()))

n, m = mi()
graph = defaultdict(list)
for _ in range(m):
    x, y = mi()
    graph[x].append(y)
    graph[y].append(x)

visited = set()
verts = [i+1 for i in range(n)]
c = 0
for vert in verts:
    if vert in visited:
        continue
    is_cycle = True
    
    deq = deque([vert])
    while deq:
        vertex = deq.pop()
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        if len(graph[vertex]) != 2:
            is_cycle = False
            
        for ver in graph[vertex]:
            deq.append(ver)
            
    if is_cycle:
        c += 1
        
print(c)