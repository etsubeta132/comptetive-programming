# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)

        freq = []
        taps = 0
        for w, f in count.items():
            freq.append((f, w))
        
        freq.sort(reverse = True)
        l = 0
        r = 1
        while l < len(freq):
            for i in range(8):
                if l < len(freq):
                    taps += r * freq[l][0]
                else:
                    break
                l += 1
            r += 1
        return taps




        
        
            


        