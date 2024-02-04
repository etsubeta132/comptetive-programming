class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        ctr = 0
        max_count = 0
        left = 0
        right = 0
        fruitType = []
        while left < len(fruits) and right < len(fruits):
            if not fruitType or (len(fruitType) < 2 and fruits[right] not in fruitType):
                fruitType.append(fruits[right])
                ctr += 1
                right += 1
            elif len(fruitType) == 2 and fruits[right] not in fruitType:
                if ctr > max_count:
                    max_count = ctr
                if max_count > len(fruits)/2:
                    return max_count
                else:
                    ctr = 0
                    left += 1
                    fruitType = []
                    right = left
            elif len(fruitType) <= 2 and fruits[right] in fruitType:
                ctr += 1
                right += 1
            if ctr > max_count:
                max_count = ctr
        return max_count