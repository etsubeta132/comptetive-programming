class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l,r = 0,0
        card = set()
        while r < len(cards) and cards[r] not in card :
            card.add(cards[r])
            r+=1
        win = float('inf')
        while r < len(cards):
            while cards[r] in card and l<r:
                win = min(win,r-l+1)
                card.remove(cards[l])
                l+=1
            card.add(cards[r])
            r+=1
        return win if win != float('inf') else -1




            