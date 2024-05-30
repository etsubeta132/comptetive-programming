from collections import defaultdict
import heapq

n, m = list(map(int, input().split()))
graph = defaultdict(list)
indegree = [0]*n

for _ in range(m):
    earlier, follower = list(map(int, input().split()))

    graph[follower].append(earlier)

    indegree[follower - 1] +=    1

queue = []
for idx, degree in enumerate(indegree):
    if degree == 0:
        queue.append(idx + 1)

heapq.heapify(queue)

order  = []
while queue:
    num = heapq.heappop(queue)
    order.append(num)

    for earlier in graph[num]:
        indegree[earlier - 1] -= 1
        if indegree[earlier - 1] == 0:
            heapq.heappush(queue, earlier)
if order:
    print(*order[::-1])
else:
    print(-1)
