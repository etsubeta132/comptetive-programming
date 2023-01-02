class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        left = 0
        right = len(tokens) - 1
        score = 0
        maxScore = 0
        tokens.sort()
        while left < right:
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            elif left < right and power < tokens[left] and score < 1:
                return score
            if score > maxScore:
                maxScore = score
        if left == right and power >= tokens[left]:
            score += 1
        if score > maxScore:
            maxScore = score
        return maxScore
