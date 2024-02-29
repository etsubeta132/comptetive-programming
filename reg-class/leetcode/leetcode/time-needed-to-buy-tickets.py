class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ctr = 0
        queue = deque([(i,tickets[i]) for i in range(len(tickets))])

        while True:
            i,per = queue.popleft()
            per-=1
            ctr+=1
            if per == 0:
                if i == k:
                    return ctr
            else:
                queue.append((i,per))



