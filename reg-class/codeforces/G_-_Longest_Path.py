nodes, edges = map(int, input().split())
graph = {i:[] for i in range(1, nodes + 1)}
degree = [0] * (nodes + 1)

for i in range(edges):
    a, b = map(int, input().split())
    graph[b].append(a)
    degree[a] += 1

distances = [-1] * (nodes + 1)

stack = []

for node in range(1, nodes + 1):
    if degree[node] == 0:
        stack.append(node)
        distances[node] = 0

for node in stack:
    for child in graph[node]:
        degree[child] -= 1
        distances[child] = max(distances[child], distances[node] + 1)
        if degree[child] == 0:
            stack.append(child)

result = max(distances) if max(distances) != -1 else 0

print(result)

