class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        m = len(queries)
        nums.sort()
        for_lst = [nums[0]]
        for i in range(1, n):
            for_lst.append(nums[i] + for_lst[ i -1])
        ctr = []
        for i in range(m):
            isSeq = False
            for j in range(len(for_lst) - 1, -1, -1):
                if for_lst[j] <= queries[i]:
                    ctr.append(len(nums[: j + 1]))
                    isSeq = True
                    break
            if not isSeq:
                ctr.append(0)
        return ctr
