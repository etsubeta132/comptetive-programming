class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for_lst = [1]
        for i in range(1, n):
            for_lst.append((i + 1) + for_lst[i - 1])
        back_sum = 0
        pivot_index = None
        while n > 0:
            back_sum += n
            if for_lst[n - 1] == back_sum:
                pivot_index = n
                break
            n -= 1
        if pivot_index is None:
            return -1
        else:
            return pivot_index
