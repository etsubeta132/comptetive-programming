import heapq

n, k, q = map(int, input().split())
friends = list(map(int, input().split()))

online_set = set()
online = []
heapq.heapify(online)

def can_join_chat(id):
    if id not in online_set:
        print("NO")
    else:
        if len(online) <= k:
            print("YES")
        else:
            lowest_friendship_level, _ = online[0]
            if friends[id - 1] >= lowest_friendship_level:
                print("YES")
            else:
                print("NO")

for _ in range(q):
    type, id = map(int, input().split())

    if type == 1:
        heapq.heappush(online, (friends[id - 1], id))
        online_set.add(id)
        if len(online) > k:
            online_set.remove(heapq.heappop(online)[1])
    
    elif type == 2:
        can_join_chat(id)
