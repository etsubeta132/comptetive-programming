import heapq
t = int(input())
hero = 0
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    total = 0
    bonus_deck = []
    heapq.heapify(bonus_deck)

    for card in cards:
        if card > 0:
            heapq.heappush(bonus_deck, -1*(card))
        else:
            if bonus_deck:
                val = heapq.heappop(bonus_deck) * (-1)

                total +=  val + card
    print(total)
