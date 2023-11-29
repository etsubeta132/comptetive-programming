class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        left = 0
        right = len(people) - 1
        count = 0
        people.sort()
        if left == right:
                count += 1
        while left < right:
            total = people[left] + people[right]
            if total > limit:
                right -= 1
                count += 1
            else:
                left += 1
                right -= 1
                count += 1
        if left == right:
                count += 1
        return count
